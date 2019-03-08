import math
def order(list) :
    if len(list) == 1 :
        a_result.append(list[0])
        Result.extend(a_result)
        del a_result[-2]
        return
    for i in list :
        a_result.append(i)
        list000 = [j for j in list if j != i]
        order(list000)
        del a_result[-1]
L = []
a_result = []
Result = []
while 1 :
    try :    
        a = int(input('输入任意个不同的整数,输入其他值时停止'))
    except :
        break
    if a in L :
        break
    L.append(a)    
lenth = len(L)
order(L)
j = 0
while j < (math.factorial(lenth)) * (lenth):
    print(Result[j:j + lenth])
    j += lenth