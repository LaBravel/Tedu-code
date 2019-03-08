def mysum(n) :
    if n == 0 :
        return 0 
    x = mypow(n)
    return x + mysum(n - 1)
def mypow(m) :
    if m == 0 :
        return 1
    return m * mypow(m-1)
print(mysum(20))