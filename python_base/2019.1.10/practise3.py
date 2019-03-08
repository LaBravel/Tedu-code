def input_number() :
    L = []
    while 1 :
        x = int(input("输入一个整数"))
        if x < 0 :
            return L
            break
        L.append(x)     
L = input_number()
print(
    "用户输入的最大数是：",max(L),
    "用户输入的最小数是：",min(L),
    "用户输入的全部数的和是：",sum(L)
)
