L = []
a = 'ABC'
b = 'XYZ'
def aaa(a,b) :
    for i in a :
        for j in b  :
            if (i == 'A' and j == 'X')  or (i == 'C' and (j == 'X' or j == 'Y') ) :
                continue
            else :
                L.append({i : j})
                c = a.replace(i,'')
                d = b.replace(j,'')
                return (c,d)
aaa(*aaa(*aaa(a,b)))
print(L)
