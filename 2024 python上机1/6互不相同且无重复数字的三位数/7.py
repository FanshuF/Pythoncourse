num = [0,0,0]
for i in range(3):
    num[i] = int(input())
for k in range(2):
    for i in range(2):
        if num[i] >= num[i+1]:
            x=num[i+1]
            num[i+1]=num[i]
            num[i]=x
print(num)