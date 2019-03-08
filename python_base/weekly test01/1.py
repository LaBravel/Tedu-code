x = 123
i = 0
while 123 <= x <= 432 :
    a = round(x * 0.01,0) #百位数字
    b = x - a * 100 #去掉百位
    c = round(b * 0.1,0) #十位数字
    d = b - c * 10 #个位数字
    if (c == 1 or c == 2 or c == 3 or c == 4) and (d == 1 or d == 2 or d == 3 or d == 4) and (a != c and d != c and a != d) :
        print(x,end =' ')
        x += 1
        i += 1
    else :
        x += 1
else :
    print('\n',"共有",i,"个不同的数字",sep = '')
