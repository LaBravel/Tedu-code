x = input("输入一串字符")
y = len(x)
print("第一个字符是：",x[0])
print("最后一个字符是：",x[-1])
if len(x) % 2 == 1 :
    print("中间的字符是:",x[y // 2])
else :
    pass
