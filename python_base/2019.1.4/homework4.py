n = int(input("输入一个整数"))
a = 1
b = 1
i = 1
c = 0
while b <= (2 * n - 1) :
    if i % 2 != 0 :
        c += a/b
        b += 2
        i += 1
    else :
        c -= a/b
        b += 2
        i += 1
else :
    print(c)
    print(c * 4)