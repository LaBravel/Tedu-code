L = []
x = 1
y = 0
for i in range(0,20) :
    x += y
    L.append(x)
    y += x
    L.append(y)
print(L)
