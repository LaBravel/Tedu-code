def mymax(*args) :
    sorted(args)
    return args[-1]
L = []
while 1 :
    a = input('shuru')
    if a == '' :
        break
    L.append(float(a))
print(mymax(*L))
