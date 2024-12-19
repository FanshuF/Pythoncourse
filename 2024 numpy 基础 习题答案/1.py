import numpy as np

# 1:
arr = np.array(range(32)).reshape(8, 4)
print(arr)

# 2:
arr2 = np.linspace(1, 2, 3)
print(arr2)

# 3:
arr3 = np.identity(9)  # 9*9的方阵
arr31 = np.eye(9)
print(arr3)

# 4：
arr4 = np.zeros(3)
print(arr4)

# 5:
arr5 = np.random.randint(1, 10, (2, 2))
print(arr5)
