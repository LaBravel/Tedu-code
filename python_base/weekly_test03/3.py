def index_type(i) :
    return type(i) is int

def turn_type(i) :
    return str(i)

L = [1,2,3,'hello','world',6,7]
L = [i for i in map(turn_type,[j for j in filter(index_type,L)])]
print(L)