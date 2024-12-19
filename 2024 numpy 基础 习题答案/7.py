import numpy as np
# 1:
obj1 = np.array([range(5)]*5)
print(obj1)
# 2:
obj2 = np.linspace(0, 1, 12)
print(obj2)
# 3:
obj3 = np.random.rand(10)
print(np.sort(obj3))
# 4:
"""
np.argwhere(条件)->好像列表推导式
只用np.argmax()只能返回第一个下标
"""
arr = np.random.randint(1,10,10)
print(arr)
all_index_max1 = np.argwhere(arr == np.max(arr))
all_index_max = np.argwhere(arr == np.max(arr)).reshape(-1)  # 通过reshape(-1)转置
arr[all_index_max1] = 0
print(arr)
