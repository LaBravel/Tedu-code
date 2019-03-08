L = [1,2,3]
def f(n = 0,lst = None) :
    if lst is None :
        lst = []
    lst.append(n)
    print(L)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)