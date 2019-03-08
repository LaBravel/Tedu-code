def myinteger(n) :
    i = 0
    while i < n :
        yield i
        i += 1
for x in myinteger(3) :
    print(x)