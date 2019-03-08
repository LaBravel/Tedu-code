D = {}
while 1 :
    x = input("输入单词")
    if x == '' :
        print(D)
        break
    y = input("输入解释")
    D[x] = y
while 1 :
    z = input("输入查询的单词")
    if z in D :
        print("解释为",D[z])
    else :
        print("查无此词")

    
    