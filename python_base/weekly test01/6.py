a = int(input("输入一个数字"))
b = int(input("输入一个数字"))
c = int(input("输入一个数字"))
if a <= b and a <= c:
    if b <= c :
        print(a,b,c,sep = ' ')
    else :
        print(a,c,b,sep = ' ')
if b <= a and b <= c:
    if a <= c :
        print(b,a,c,sep = ' ')
    else :
        print(b,c,a,sep = ' ')
else :
    if a <= b :
        print(c,a,b,sep = ' ')
    else :
        print(c,b,a,sep = ' ')    