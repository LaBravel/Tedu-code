def classify(x) :
    a = int(x * 0.01)# 百位数
    b = int((x - a * 100) * 0.1)#十位数
    c = int((x - a * 100 - b * 10))#个位数
    return [a,b,c]
def calculate(a,b,c) :
    return a ** 3 + b ** 3 + c ** 3
for i in range(100,1000) :
    L = classify(i)
    if calculate(*L) == i :
        print(i,end = '  ')
