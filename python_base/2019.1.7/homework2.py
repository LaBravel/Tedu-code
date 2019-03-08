x = int(input("输入一个整数"))
j = 0
for i in range(2,x) :
    if x % i != 0 :
        continue
    else :
        j = 1
if j == 0 :
    print(x,'是素数')
else :
    print(x,'不是素数')