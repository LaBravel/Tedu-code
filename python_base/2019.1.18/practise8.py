s = {'唐僧','悟空','八戒','沙僧'}
a = iter(s)
try :
    while 1 :
        print(next(a))
except :
    print('遍历结束')