def myrange(start,stop = 0,step = 1) :
    if stop == 0 :
        stop = start
        start = 0
    while start < stop :
        yield start
        start += step

print(sum(x ** 2 for x in myrange(1,10) if x % 2))