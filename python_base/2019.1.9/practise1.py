seasons = {
    1:'春季有1 2 3月',
    2:'夏季有4 5 6月',
    3:'秋季有7 8 9月',
    4:'冬季有10 11 12月'
}
a = int(input("输入一个整数(1-4)"))
if a in seasons :
    print(seasons[a])
else :
    print("信息不存在")