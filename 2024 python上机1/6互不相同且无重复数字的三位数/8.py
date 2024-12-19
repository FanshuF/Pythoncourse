import math
def judge(num):
    det = int(math.sqrt(num))
    if det * det == num:
        return 1
    else:
        return 0
for i in range(10000):
    num1 = i+100
    num2 = i+268
    if judge(num1) == 1 and judge(num2) == 1:
        print(i)
