x = int(input("输入一个年份"))
if x % 4 == 0 and x % 100 != 0 :
    print("这是闰年")
elif x % 4 == 0 and x % 100 == 0 and  x % 400 == 0 :
    print("这是闰年")
else :
    print("这不是闰年")