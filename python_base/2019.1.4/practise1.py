a = input("输入第一行文字")
b = input("输入第二行文字")
c = input("输入第三行文字")
l = str(max(len(a),len(b),len(c)))
x = '%' + l + 's'
print(x % a)
print(x % b)
print(x % c)

