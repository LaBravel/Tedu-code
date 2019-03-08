def cal() :
    global a
    for i in range(2,a) :
        if a % i == 0 :
            L.append(i)
            a = int(a / i)
            break
        elif i == a - 1 :
            L.append(a)
            a = 1
            break
        continue

a = int(input('输入一个正整数'))
b = a
L = []
while 1 :
    if a == 1 :
        L1 = ['%d' % i for i in L]
        print(b,'=',('*'.join(L1)))
        break
    cal()
        
