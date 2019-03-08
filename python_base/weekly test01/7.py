y = int(input("输入年份"))
m = int(input("输入月份"))
d = int(input("输入日期"))
a = '312831303130313130313031'
b = '312931303130313130313031'
i = 0
j = 1
x = 0
if y % 400 == 0 or (y % 4 ==0 and y % 100 != 0):
    if m == 1 :
        print("这是第",d,"天")
    elif 1 < m < 13 :
        while j < m :
            x += int(b[i:i+2])
            i += 2
            j += 1
        else :    
            print("这是第",x + d,"天")        
else :
    if m == 1 :
        print("这是第",d,"天")
    elif 1 < m < 13 :
        while j < m :
            x += int(a[i:i+2])
            i += 2
            j += 1
        else :    
            print("这是第",x + d,"天") 