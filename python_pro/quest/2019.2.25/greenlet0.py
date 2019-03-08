from greenlet import greenlet

def test1() :
    print('执行test1')
    g2.switch()
    print('结束test1')

def test2() :
    print('执行test2')
    g1.switch()
    print('结束test2')

#将这两个函数变成协程
g1 = greenlet(test1)
g2 = greenlet(test2)

g2.switch()
g1.switch()