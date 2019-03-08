x = int(input("输入一个正整数"))
w = 2 * x - 1
for i in range(1,w + 1,2) :
    y = '*' * i
    print(y.center(w))
y = '*'
i = 1
while i <= x :
    print(y.center(w))
    i += 1