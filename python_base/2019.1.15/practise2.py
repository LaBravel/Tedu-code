def sushu(n) :
    for i in range(2,n) :
        if n % i == 0 :
            return False
    return True

L = [i for i in filter(sushu,range(1,101))]
print(L)