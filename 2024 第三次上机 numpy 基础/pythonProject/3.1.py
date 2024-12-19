import numpy as np
filepath = r'D:\wpsfinished\大三上\python\2024 第三次上机 numpy 基础\pythonProject\AAPL.csv'
c, v = np.loadtxt(filepath, delimiter=',', usecols=(4, 5), unpack=True, skiprows=1)
weighted_avg_price = np.average(c, weights=v)#计算成交量的加权平均价格
print("成交量的加权平均价格:", weighted_avg_price)

close_price_avg = np.mean(c)#计算收盘价的平均价格
print("收盘价的平均价格:", close_price_avg)

weights = np.linspace(1, len(v), len(v))# 创建一个权重数组，时间越近权重越大
time_weighted_avg_price = np.average(c, weights=weights)#计算收盘的加权平均价格
print("时间加权平均价格:", time_weighted_avg_price)

max_price = np.max(c)#寻找最大值和最小值
min_price = np.min(c)
price_range = max_price - min_price
print("最高收盘价:", max_price)
print("最低收盘价:", min_price)
print("收盘价的极值波动范围:", price_range)

median_price = np.median(c)#计算收盘价的中位数和方差
price_variance = np.var(c)
print("收盘价的中位数:", median_price)
print("收盘价的方差:", price_variance)

#计算普通收益率和对数收益率以及收益波动率
# 普通收益率
simple_returns = np.diff(c) / c[:-1]
print("普通收益率:", simple_returns)

# 对数收益率
log_returns = np.diff(np.log(c))
print("对数收益率:", log_returns)

# 收益波动率
# 计算对数收益率的标准差
log_returns_std = np.std(log_returns)
# 年化波动率
annualized_volatility = log_returns_std * np.sqrt(252)
print("年化波动率:", annualized_volatility)