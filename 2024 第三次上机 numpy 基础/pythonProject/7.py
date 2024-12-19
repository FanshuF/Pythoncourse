import numpy as np

a = np.arange(5)
am = np.tile(a, (5, 1))
print(am)  #(1)

b = np.linspace(0, 1, 12)
print(b)  #(2)

c = np.random.rand(10)
d = np.sort(c)
print(d)  #(3)

e=np.random.rand(10)
print("原=")
print(e)
e[np.argmax(c)] = 0
print("去max=")
print(e)