a = 1
b = 1
while b <= 9 :
    while a <= b :
        c = a * b
        print(a,'x',b,'=','%-2d' % c,end = '  ',sep = '')
        a += 1
    else :
        print()
    b += 1
    a = 1
