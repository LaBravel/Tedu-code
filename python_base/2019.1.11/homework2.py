i = 1
x = 2
D = []
while i <= 4 :
    L = []
    for j in range(1,x) :
        if x % j == 0 :
            L.append(j)
    if sum(L) == x :
        print(x,"是完全数")
        print(L)
        i += 1
    x += 1