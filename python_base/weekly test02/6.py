MONTH1 = [31,29,31,30,31,30,31,31,30,31,30,31]
MONTH2 = [31,28,31,30,31,30,31,31,30,31,30,31]
def year(z) :
    x = 0
    for z in range(1,z) :
        if (z % 400 == 0) or (z % 4 == 0 and z % 100 != 0) :
            x += 366
        else :
            x += 365
    return x
def month(z,y) :
    x = 0
    for y in range(1,y) :
        if (z % 400 == 0) or (z % 4 == 0 and z % 100 != 0) :
            x += MONTH1[y - 1]
        else :
            x += MONTH2[y - 1]
    return x
def day(x) :
    return x 
L = [
    int(input("输入年份")),
    int(input("输入月份")),
    int(input("输入日期"))
    ]
print('这是第',year(L[0]) + month(L[0],L[1]) + day(L[2]),'天')

    