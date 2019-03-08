def triangle(L) :
    LM = []
    LM.extend(L)
    LP = ['%d' % i for i in L]
    print((' '.join(LP)).center(20))
    l = len(LM)
    for i in range(len(LM) - 1) :
        L[i + 1] = (LM[i] + LM[i + 1])
    L.append(1)
    LM.clear()
    LP.clear()

L = [1]
for i in range(6) :
# while 1 :
#     a = input('按回车打印一行杨辉三角形')
#     if a == '' :
    triangle(L)
        