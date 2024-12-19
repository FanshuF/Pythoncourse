import numpy as np
arr = np.arange(10)
print(arr[1],arr[2]) #(1)


arr[4:7] = 12 #(2)
print(arr)

arr[5:]=12 #(3)
print(arr)