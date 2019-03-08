for i in range(-100,9999) :
    n1 = (i + 100) ** 0.5
    n2 = (i + 268) ** 0.5
    if n1 == round(n1,0) and n2 == round(n2,0) :
        print(i)
else :
    pass
