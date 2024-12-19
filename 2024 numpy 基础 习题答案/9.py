import numpy as np
x = np.array([[0,1,2],[3,4,5],[6,7,8]])
 
b = np.append(x,[[7,8,9]],axis=0)      # 插入一行
c = np.append(x,[[7],[8],[9]],axis=1)  # 插入一列
 
print(b)
print(c)
