import numpy as np

# 创建一个3x3的ndarray对象
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("原始数组:\n", a)
b = np.append(a, [[7, 8, 9]], axis=0)
print("行扩充后的数组:\n", b)
c = np.append(a, [[7], [8], [9]], axis=1)
print("列扩充后的数组:\n", c)