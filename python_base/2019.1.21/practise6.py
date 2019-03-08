def mymap(fn,iterable) :
    for i in iterable :
        yield fn(i)

L = [i for i in map(lambda x : x * 2,range(10))]
print(L)