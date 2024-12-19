import numpy as np
z = np.genfromtxt("data.txt", delimiter=",")
print("矩阵z:\n", z)
# 将z转置得到X
X = z.T
print("矩阵x:\n", X)
Y = X.T
print("矩阵Y:\n", Y)
# 计算矩阵X乘以矩阵Y的结果
result = X @ Y
print("矩阵X乘以矩阵Y的结果:\n", result)
num = X * Y.T
print("矩阵X和Y的逐元素乘积:\n", num)
def find(target):
    diff = np.abs(X - target)  # 计算绝对差值
    min_diff = np.nanmin(diff)  # 忽略NaN，找到最小差值
    if min_diff == 0:
        return target  # 如果差值为0，说明找到了target
    else:
        return X[np.unravel_index(np.argmin(diff, axis=None), X.shape)]  # 返回最接近target的值

# 测试函数
print("查找数字9的结果:", find(9))
print("查找数字100的结果:", find(100))