a = int(input("请输入一个数"))
b = a
print('@' * a)
while (b - 2) > 0 :
    print('@'+' ' * (a - 3),'@')
    b -= 1
else :
    print('@' * a)