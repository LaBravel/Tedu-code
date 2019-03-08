def mydeco(fn) :
    def fx() :
        print('----------------')
        fn()
        print('+++++++++++++++')
    return fx
@mydeco        
def myfunc() :
    print('函数myfunc被调用')
# myfunc = mydeco(myfunc)
myfunc()
myfunc()
myfunc()