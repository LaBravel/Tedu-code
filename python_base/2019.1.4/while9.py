a = int(input("输入三角形的底和高"))
i = 1
while i <= a :#第一题
    print('*' * i)
    i += 1
else :
    i = 1

while i <= a :#第二题
    print(' ' * (a - i) + '*' * i)
    i += 1
else :
    i = 0

while i < a :#第三题
    print(' ' * i  + '*' * (a - i))
    i += 1
else :
    i = 0

while i <= a :#第四题
    print('*' * (a - i) + ' '* i)
    i += 1
else :
    pass