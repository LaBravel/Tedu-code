import random

def quick_sort(list) :
    if len(list) == 0 :
        return
    temp = random.choice(list)
    quick_sort([i for i in list if i < temp])
    result.append(temp)
    quick_sort([i for i in list if i > temp])

if __name__ == '__main__' :
    L = random.sample([i for i in range(100)],10)
    result = []
    print('快速排序前:',L)
    quick_sort(L)
    print('快速排序后:',result)