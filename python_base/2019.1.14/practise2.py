def fn_outer() :
    print('fn_outer被调用')
    def fn_inner() :
        print('fn_inner被调用')
        print('fn_inner调用结束')
    print('fn_outer调用结束')
    return fn_inner
fn = fn_outer() 
fn()
