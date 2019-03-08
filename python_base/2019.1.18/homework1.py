s = 0
h = 100
for i in range(10) :
    s += h
    h = h / 2
    s += h
print(h)
print(s)
