l1 = ['黑桃' + str(i) for i in range(1,14)]
x = 0 
def query(L,key) :
    global x
    index = (len(L)) // 2 - 1
    print(index)
    if int(L[index][2]) == key :
        print('找到啦,共进行',x,'次二分')
        return
    elif int(L[index][2]) > key :
        L = L[0:index - 1]
    elif int(L[index][2]) < key :
        L = L[index + 1:-1]
    x += 1
    return query(L,key)

if __name__ == '__main__' :
    query(l1,12)

