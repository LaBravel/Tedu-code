L = []
while 1 :
    a = int(input("输入正整数"))
    if a != -1 and a > 0 :
        L += [a]
    elif a == -1 :
        break
print(len(L),"个有效的数")
print("最大数是",max(L))
print("最小数是",min(L))
print("平均数是",sum(L) / len(L))