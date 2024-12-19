'''
规则：
在总成绩相同是，优先录取数学成绩高的学生；
若总成绩和数学成绩都相同时，按照英语成绩高的学生进行优先录取;
最后，按照英语、数学和总成绩进行升序排序。
'''
import numpy as np
math=np.array([101,109,115,108,118,118])  #数学成绩
en=np.array([117,105,118,108,98,109])     #英语成绩
total=np.array([621,623,620,620,615,615]) #总成绩
print(math)
print(en)
print(total)
sort_total=np.lexsort((en,math,total))    #用lexsort函数对多个序列进行排序
print('排序后的索引值:')
print(sort_total)
print ('通过排序后的索引获取排序后的数组：')
print(np.array([[en[i],math[i],total[i]] for i in sort_total]))
