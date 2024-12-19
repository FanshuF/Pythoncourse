import numpy as np
# 1:
a = np.random.randn(10)
print(np.where(a > 0, 1, -1))
 
# 2:
x = np.array([[0,7,9,5,8,1,2,6,0,4]])
print(np.piecewise(x, [x<3, ((x>3)&(x<5)), x>7], [-1, 1, lambda x:x*4]))
