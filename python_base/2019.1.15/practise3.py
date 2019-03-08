def aaa(x) :
    return ''.join([i for i in reversed(x)])
names = ['Tom','Jerry','Spike','Tyke']
L = sorted(names,key = aaa)
print(L)