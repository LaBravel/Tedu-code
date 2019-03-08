def mysum(n) :
    if n == 0 :
        return 0
    else :
        return n + mysum(n - 1)
print(mysum(100))