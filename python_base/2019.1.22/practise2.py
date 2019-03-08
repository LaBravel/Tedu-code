def mywrite(list) :
    info = open('si.txt','w')
    for i in list :
        info.write('%s,%d,%d\n' % (i['name'],i['age'],i['score']))
    info.close

L = [dict(name = 'xiaozhang',age = 20,score = 100),
    dict(name = 'xiaoli',age = 18,score = 98)
    ]
mywrite(L)
