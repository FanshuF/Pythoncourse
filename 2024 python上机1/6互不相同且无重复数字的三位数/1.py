cnt=0
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            if i!=j and j!=k and i!=k:
                cnt=cnt+1
                num = 100*i+10*j+k
                print("第%d个：%d"%(cnt,num))

print("共有 %d 个"%cnt)
