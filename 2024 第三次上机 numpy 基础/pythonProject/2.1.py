import numpy as np
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
num1= np.sum(a)
print("sum:")
print(num1)#(1)

num2 = a.sum(axis=0)
print("sum0:")
print(num2)
num3 = a.sum(axis=1)
print("sum1:")
print(num3)#(2)

num4 = np.mean(a)
print("mean:")
print(num4)#(3)

mean0 = a.mean(axis=0)
print("mean0:")
print(mean0)
mean1 = a.mean(axis=1)
print("mean1:")
print(mean1)#(4)

num4= np.max(a)
print(num4)#(5)

print(a.max(axis=0),a.max(axis=1))#(6)