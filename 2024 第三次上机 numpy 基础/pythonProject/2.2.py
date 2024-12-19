import numpy as np

# 创建单价和销量数组
price = np.array([34.5, 36, 37.8, 39, 39.8, 33.6])
number = np.array([900, 580, 230, 150, 120, 1800])

# 计算加权平均价格
avg = np.sum(price * number) / np.sum(number)

print("加权平均价格:", avg)

# 对price数组进行排序
sortprice = np.sort(price)

# 计算排序后的中位数
median_price = np.median(sortprice)

# 计算排序后的方差
variance_price = np.var(sortprice)

# 计算排序后的标准差
std_price = np.std(sortprice)

print("排序后的中位数:", median_price)
print("排序后的方差:", variance_price)
print("排序后的标准差:", std_price)