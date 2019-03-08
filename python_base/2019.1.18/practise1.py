def div_apple(n) :
    print(n,'个苹果你想分给几个人?')
    s = input('请输入人数')
    cnt = int(s)#可能触发ＶalueＥrror错误
    result = n / cnt#可能触发ZeroDivsionError错误
    print('每个人分了',result,'个苹果')

try :
    div_apple(10)
    print('分苹果成功')
except ValueError :
    print('分苹果失败，苹果被收回')
except :
    print('其他类型的错误发生，苹果被收回')
finally :
    print('此这是try语句中的finally语句,一定会被执行')
print('程序正常退出')