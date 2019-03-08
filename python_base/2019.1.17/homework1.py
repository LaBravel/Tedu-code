L = [chr(i) for i in range(97,123)]
L.extend([chr(j) for j in range(65,91)])
L.extend(range(0,10))
def password() :
    import random
    a = []
    for i in range(6) :
        a += [random.choice(L)]
    return a
print(password())
