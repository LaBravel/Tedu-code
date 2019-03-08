L = [3,5]
L = list(range(1,3)) + L
L[2:] = range(3,7)
print(L)
L[::-1] = [i for i in L]
del L[len(L)-1] 
print(L)