x = int(input('输入一个整数'))
for i in range(1,x + 1) :    
    for j in range(1,x + 1) :
        print("%-2d" % j,end = ' ')
    else :
        print()
print('---------------------------------------')
k = 0
for i in range(1,x + 1) :
    for j in range(i,x + i) :
        print("%-2d" % j,end = ' ')
    else :
        print()