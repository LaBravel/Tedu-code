# x = input("输入一串字符")
# print(x[1:-1])

x = input("输入一串字符")
if x[::1] == x[::-1] :
    print(x,"是回文")
else :
    print(x,"不是回文")
