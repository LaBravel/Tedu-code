L = []
while 1 :
    x = int(input("输入一个正整数"))
    if x >= 0 :
        L += [x]
    elif x < 0 :
        break
print(L)