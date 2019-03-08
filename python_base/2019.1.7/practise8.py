x = 1
X = [1]
L = []
for x in X :
    a = int(input("shuru"))
    if a >= 0 :
        L += [a]
    elif a < 0 :
        break
    X+= [1] 
print(L)