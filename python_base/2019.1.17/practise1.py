import random,sys
x = random.randint(0,100)
i = 1
for y in sys.stdin :
    if int(y) == x :
        print('恭喜您猜对了')
        print('一共猜了',i,'次')
        break
    elif int(y) >= x :
        print('您猜大了')
    elif int(y) <= x :
        print('您猜小了')   
    i += 1