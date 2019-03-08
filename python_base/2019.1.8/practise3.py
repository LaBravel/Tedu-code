L = []
while 1 :
    a = int(input("输入一个正整数"))
    if a < 0 or a in L :
        break
    L += [a]
if len(L) >= 2 :
    print("这些数的和是",sum(L))
    print("这些数的最大数是",max(L))
    print("这些数的最二大数是",sorted(L)[-2])
    L.remove(min(L))
    print("删除最小数后的列表为",L)
else :
    print("您输入的数字不够")

