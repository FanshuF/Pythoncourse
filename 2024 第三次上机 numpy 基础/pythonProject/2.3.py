import numpy as np


math = np.array([101, 109, 115, 108, 118, 118])
en = np.array([117, 105, 118, 108, 98, 109])
total = np.array([621, 623, 620, 620, 615, 615])


records = np.stack((total, math, en), axis=-1)# 堆叠成记录数组，一行代表一个学生的成绩
num = np.lexsort((en, math, total))
total1 = total[num]
math = math[num]
en = en[num]

print("排序后的总成绩:", total1)
print("排序后的数学成绩:", math)
print("排序后的英语成绩:", en)