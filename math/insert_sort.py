import random

def insert_sort(list) :
    for i in range(1,len(list)) :
        temp = list[i]
        for j in range(i-1,-1,-1) :
            if list[j] > temp :
                list[j + 1] = list[j]
                pos = j
            else :
                pos = j + 1
                break
        list[pos] = temp
    return list



if __name__ == '__main__' :
    L = [100,90,96,87,110,120,97,93,82,88]
    random.shuffle(L)
    print('插入排序前:',L)
    print('插入排序后:',insert_sort(L))