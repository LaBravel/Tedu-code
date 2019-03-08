def myrange(*args) :
    L = []
    if len(args) == 1 :
        i = 0
        while i < args[0] :
            L.append(i)
            i += 1
    if len(args) == 2 :
        i = args[0]
        while args[0] <= i < args[1] :
            L.append(i)
            i += 1
    if len(args) == 3 :
        i = args[0]
        while args[0] <= i < args[1] :
            L.append(i).
            i += args[2]
    return L
print(myrange(10))
print(myrange(2,10))
print(myrange(2,10,2))

