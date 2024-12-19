'''
故事背景：
在古印度，国王为了奖赏发明国际象棋的大臣，对他说：“我可以满足你的任何要求。”，大臣说：
“请给我的棋盘的64个格子都放上小麦，第一个格子放1粒小麦，第二个格子放2粒，第三个放4粒，依次类推，
后面每个格子放的小麦粒数都是前一个格子里放的2倍，直到第64个格子。

实质：
使用NumPy的logspace函数来创建这个问题中所描述的等比数列。
'''
import numpy as np

#输出时打印不换行
np.set_printoptions(linewidth=750)
#n = np.logspace(0,63,64,base=2,dtype='int')

n = np.logspace(0, 63, 64, base = 2,dtype='uint64')

#数组重塑8*8矩阵
print(n.reshape(8,8))
