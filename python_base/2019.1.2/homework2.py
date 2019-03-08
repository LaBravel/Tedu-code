a,b,c = map(float,input("输入三个数字").split())
if a >= b :
    if a >= c :
        print("最大数是",a)
    elif a < c :
        print("最大数是",c)
if a < b :
    if b >= c :
        print("最大数是",b)
    elif b < c :
        print("最大数是",c)

    