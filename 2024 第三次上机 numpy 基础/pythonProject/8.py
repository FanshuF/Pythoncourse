import numpy as np

a=np.random.randn(10)
print(a)
a = np.where(a > 0, 1, -1)
print(a) #(1)

b=np.array([[0,7,9,5,8,1,2,6,0,4]])
print(b)
b = np.piecewise(b,
    [b < 3, (b >= 3) & (b < 5), b > 7],
    [lambda b: -1, lambda b: 1, lambda b: b * 4])
print(b)