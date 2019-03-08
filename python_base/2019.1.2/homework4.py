a,b,c = map(int,input("输入三个整数").split())
if a > b and a > c :
    if b > c :
        print("三个数字排序为",a,">",b,">",c)
    elif b < c :
        print("三个数字排序为",a,">",c,">",b)
    elif b == c :
        print("三个数字排序为",a,">",c,"=",b)
elif b > a and b > c :
    if a > c :
        print("三个数字排序为",b,">",a,">",c)
    elif a < c :
        print("三个数字排序为",b,">",c,">",a)
    elif a == c :
        print("三个数字排序为",b,">",a,"=",c)
elif c > a and c > b :
    if a > b :
        print("三个数字排序为",c,">",a,">",b)
    elif a < b :
        print("三个数字排序为",c,">",b,">",a)
    elif a == b :
        print("三个数字排序为",c,">",b,"=",a)
elif a == b == c :
    print("三个数字排序为",c,"=",b,"=",a)
