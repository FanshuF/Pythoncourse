# -*- coding: utf-8 -*-

import numpy as np

z = np.genfromtxt("data.txt", delimiter=",")  #读取文件
print(z)
print(z.reshape(4,5))

X = np.mat(z)
Y = np.mat(z.T)
print(X*Y)  #矩阵相乘结果
'''
U, S, V = np.linalg.svd(X*Y)
rank = np.sum(S > 1e-10)
print(rank)  #r(XY)
'''
rank_XY = np.linalg.matrix_rank(X*Y)
print(rank_XY)

def find(target): #在矩阵X中查找target
    tmp = X[X == target]
    if np.size(tmp) > 0:
        print(int(tmp))
    else:
        xxx= np.argmin (np.abs(X - target))

        m = X.flat[np.abs(X - target).argmin()]
        m1 = X.flat[xxx]

        print(m)

find(9.6)

