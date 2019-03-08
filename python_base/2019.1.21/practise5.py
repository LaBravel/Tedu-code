def myfilter(fn,iterable) :
    def justify(j) :
        return fn(j)
    for i in iterable :
        if justify(i) is True :
            yield i
print([i for i in myfilter(lambda x : x % 2 ==0,range(10))])

