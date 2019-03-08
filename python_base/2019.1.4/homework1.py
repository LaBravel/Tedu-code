a = int(input("输入一个整数"))
i = 1
c = 0
while i <= a :
    if i % 2 == 0 :
        print(i)
        c += i
        i += 1
    else :
        i += 1
else :
    print("所有偶数和为：",c)