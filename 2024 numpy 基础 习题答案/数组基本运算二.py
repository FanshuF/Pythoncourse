import numpy as np
price=np.array([34.5,36,37.8,39,39.8,33.6])  #创建“单价”数组
number=np.array([900,580,230,150,120,1800])  #创建“销售数量”数组
#print('加权平均价：',np.average(price))
print('加权平均价：',np.average(price,weights=number))
# 数组排序后，查找中位数
sort_n = np.msort(price)# 从小到大排序
print('数组排序：',sort_n)
print('数组中位数为：',np.median(sort_n))
print('数组方差：',np.var(price))
print('数组标准差：',np.std(price))
