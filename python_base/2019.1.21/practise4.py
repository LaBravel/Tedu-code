L = [2,3,5,7]
def myyield_1(list) :
    for i in list :
        print(i ** 2 + 1)
myyield_1(L)

for i in (j ** 2 + 1 for j in L) :
    print(i)

print([(i ** 2 + 1) for i in L])