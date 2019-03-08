def make_except() :
    print('函数开始')
    error = ValueError('这是故意制造的错误')
    raise error
    print  ('函数结束')

try :
    make_except()
    print('make_except 调用完毕')
except ValueError :
    print('make_except函数调用发生异常')

print('程序正常退出')