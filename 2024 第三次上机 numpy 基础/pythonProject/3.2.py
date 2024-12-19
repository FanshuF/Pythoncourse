import numpy as np
filepath = r"D:\wpsfinished\大三上\python\2024 第三次上机 numpy 基础\pythonProject\亚洲国家20年人口数据-gb2312.csv"
# 读取国家,人口索引
country_index = np.array(open(filepath).readline()[:-1].split(','))
p_data = np.genfromtxt(filepath, delimiter=',', skip_header=1, dtype=float)

# 打印国家索引和人口数据的形状
print("国家索引:", country_index)
print("人口数据形状:", p_data.shape)

# 计算每个国家的人口平均值
population_mean = np.mean(p_data, axis=1)
print("每个国家的人口平均值:\n", population_mean)

# 计算每个国家的人口方差
population_variance = np.var(p_data, axis=1)
print("每个国家的人口方差:\n", population_variance)

# 计算每个国家的人口标准差
population_std = np.std(p_data, axis=1)
print("每个国家的人口标准差:\n", population_std)

# 计算每个国家的人口中位数
population_median = np.median(p_data, axis=1)
print("每个国家的人口中位数:\n", population_median)

# 计算每个国家的人口最大值和最小值
population_max = np.max(p_data, axis=1)
population_min = np.min(p_data, axis=1)
print("每个国家的人口最大值:\n", population_max)
print("每个国家的人口最小值:\n", population_min)

# 计算每个国家的人口极值波动范围
population_range = population_max - population_min
print("每个国家的人口极值波动范围:\n", population_range)