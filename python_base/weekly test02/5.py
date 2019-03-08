def calculate(i,j = 0) :
    k = i + j
    i = int(k / 2)
    j = int(k % 2)
    return [i,j]
L = [int(input("有多少钱?")),0]
num = 0
while 1 :
    num += L[0]
    L = calculate(*L)
    if sum(L) == 1 and L[0] == 1  :
        num += 1
        break
    elif sum(L) == 1 and L[1] == 1 :
        break
print("能买",num,'瓶')