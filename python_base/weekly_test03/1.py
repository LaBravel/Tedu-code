def average(dict) :
    L = [i for i in dict.values()]
    x = sum(L) / len(L)
    print('平均值＝',x)

def sorted_down(dict) :
    L = ['%s%d分' % (i,dict[i]) 
        for i in sorted(dict,key = lambda x : dict[x],reverse = True)
        ]
    print('成绩从高到低排序为:',L)

def index_max(dict) :
    L = ['%s%d分' % (i,dict[i]) 
        for i in sorted(dict,key = lambda x : dict[x],reverse = True)
        ]
    print('最高分为',L[0])

def index_min(dict) :
    L = ['%s%d分' % (i,dict[i]) 
        for i in sorted(dict,key = lambda x : dict[x],reverse = True)
        ]
    print('最低分为',L[-1])

D = {'小李':90,'小王':98,'小张':85,'小周':60}    
print('成绩单为：',D)

average(D)
sorted_down(D)
index_max(D)
index_min(D)
