import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation
import os
import matplotlib
import warnings
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
except:
    warnings.warn("未找到 SimHei 字体，请根据系统安装中文支持字体。")

# 加载数据
try:
    data = scipy.io.loadmat('横着走.mat')
    assert 'xydata' in data, "MAT文件中未找到变量 'xydata'"
    xydata = data['xydata']
    assert xydata.ndim == 3, "xydata 应为三维数组，格式为 (x, y, frame)"
    logging.info("成功加载 '横着走.mat' 文件。")
except Exception as e:
    logging.error(f"加载数据失败: {e}")
    exit(1)

# 参数设置
L_max = 8  # 最大未关联次数
hithold = 7
gate_threshold = 0.5  # 关联门限

# 卡尔曼滤波器参数
T = 1
processnoise = 0.2
measurenoise = 1

# 状态转移矩阵 F 和观测矩阵 H
F = np.array([[1, T, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, T],
              [0, 0, 0, 1]])

H = np.array([[1, 0, 0, 0],
              [0, 0, 1, 0]])

# 过程噪声协方差矩阵 Q 和观测噪声协方差矩阵 R
Q = (processnoise ** 2) * np.array([
    [T ** 3 / 3, T ** 2 / 2, 0, 0],
    [T ** 2 / 2, T, 0, 0],
    [0, 0, T ** 3 / 3, T ** 2 / 2],
    [0, 0, T ** 2 / 2, T]
])

R = (measurenoise ** 2) * np.eye(2)


# 轨迹类
class Track:
    _id_counter = 1  # 类变量，用于生成唯一ID

    def __init__(self, initial_position, frame):
        self.id = Track._id_counter
        Track._id_counter += 1
        self.state = np.array([initial_position[0], 0, initial_position[1], 0]).reshape(4, 1)
        self.covariance = np.eye(4) * 100
        self.history = [initial_position]
        self.livetime = 0
        self.hits = 1
        self.creation_frame = frame

    def predict(self):
        self.state = F @ self.state
        self.covariance = F @ self.covariance @ F.T + Q

    def update(self, detection):
        S = H @ self.covariance @ H.T + R
        K = self.covariance @ H.T @ np.linalg.inv(S)
        z = np.array(detection).reshape(2, 1)
        y = z - (H @ self.state)
        self.state = self.state + K @ y
        self.covariance = (np.eye(len(self.state)) - K @ H) @ self.covariance
        self.history.append(detection)
        self.livetime = 0
        self.hits += 1

        # 限制 history 的长度不超过10
        if len(self.history) > 10:
            self.history.pop(0)

    def increment_livetime(self):
        self.livetime += 1
        if len(self.history) > 10:
            self.history.pop(0)


# 辅助函数
def update_tracks(tracks, detections):
    updated_tracks = []
    remaining_detections = detections.copy()
    for track in tracks:
        track.predict()
        min_distance = np.inf
        best_detection = None
        best_idx = -1
        for idx, detection in enumerate(remaining_detections):
            predicted_pos = H @ track.state
            distance = np.linalg.norm(detection - predicted_pos.flatten()[:2])
            if distance < min_distance:
                min_distance = distance
                best_detection = detection
                best_idx = idx
        if min_distance < gate_threshold:
            track.update(best_detection)
            updated_tracks.append(track)
            if best_idx >= 0:
                remaining_detections = np.delete(remaining_detections, best_idx, axis=0)
        else:
            track.increment_livetime()
            updated_tracks.append(track)
    return updated_tracks, remaining_detections


def plot_tracking(cf_tracks, sumpoint, frame_num, colors, ax, legends):
    ax.cla()
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 3)
    ax.set_xlabel('X 坐标')
    ax.set_ylabel('Y 坐标')
    ax.set_title(f'使用卡尔曼滤波器的目标跟踪 - 帧 {frame_num}')
    ax.grid(True)

    # 绘制当前检测点
    if sumpoint.size > 0:
        ax.scatter(sumpoint[:, 0], sumpoint[:, 1], s=100, marker='s', color=[0.1, 0.9, 0.5], label='检测点')

    # 绘制已确认的轨迹
    for track in cf_tracks:
        color = colors[(track.id - 1) % len(colors)]
        history = np.array(track.history)
        ax.plot(history[:, 0], history[:, 1], 'o-', color=color, linewidth=2, label=f'目标 {track.id}')

    # 处理图例，避免重复
    if legends is not None:
        legends.remove()
    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys(), loc='upper right')


def main():
    cf_tracks = []
    temp_tracks = []
    all_tracks = []
    frames = xydata.shape[2]


    import matplotlib.cm as cm
    cmap = cm.get_cmap('hsv', 100)
    colors = [cmap(i) for i in range(100)]

    fig, ax = plt.subplots(figsize=(8, 6))

    # 初始化图例句柄
    legends = None

    # 定义初始化函数
    def init():
        ax.set_xlim(-3, 3)
        ax.set_ylim(0, 3)
        ax.set_xlabel('X 坐标')
        ax.set_ylabel('Y 坐标')
        ax.set_title('使用卡尔曼滤波器的目标跟踪')
        ax.grid(True)
        return []

    # 定义动画更新函数
    def animate(i):
        nonlocal cf_tracks, temp_tracks, all_tracks, legends
        # 处理前42帧外的帧
        if i >= frames - 42:
            return []

        sumpoint = xydata[:, :, i]
        sumpoint = sumpoint[~((sumpoint[:, 0] == 0) & (sumpoint[:, 1] == 0))]

        if np.any((sumpoint[:, 0] == 0) & (sumpoint[:, 1] == 0)):
            logging.warning(f'警告: 第 {i + 1} 帧中仍存在 (0, 0) 的点。')

        # 更新已确认轨迹和临时轨迹
        all_tracks = cf_tracks + temp_tracks
        all_tracks, remaining_detections = update_tracks(all_tracks, sumpoint)

        # 分离已确认轨迹和临时轨迹
        cf_tracks = [track for track in all_tracks if track.hits >= hithold]
        temp_tracks = [track for track in all_tracks if track.hits < hithold and track.livetime <= L_max]

        # 创建新轨迹
        if remaining_detections.size > 0:
            for det in remaining_detections:
                new_track = Track(det, i + 1)
                temp_tracks.append(new_track)
                logging.info(f'创建新轨迹，ID: {new_track.id}, 帧: {i + 1}, 位置: ({det[0]:.2f}, {det[1]:.2f})')

        # 绘制跟踪结果
        plot_tracking(cf_tracks, remaining_detections, i + 1, colors, ax, legends)

        return []

    # 创建动画
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frames - 42, interval=50, blit=False)

    # 保存动画为 GIF
    anim.save('tracking_animation.gif', writer='pillow', fps=20)

    logging.info("GIF 动画已保存为 'tracking_animation.gif'。")
    plt.close()


if __name__ == "__main__":
    main()
