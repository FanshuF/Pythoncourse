import numpy as np
arr = np.arange(10)
# 1:
print(arr[1], arr[2])
 
# 2:
arr[4:7] = 12
print(arr)
 
# 3:
arr[5:] = 10
print(arr)
