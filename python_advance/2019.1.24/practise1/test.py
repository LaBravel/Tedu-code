from Phone import *
class Test(Phone) :
    pass

mytest = Test('锤子',999,'i3处理器',14)
mytest.startup()
mytest.call()
mytest.send_msg()
mytest.print_info()
mytest.shutdown()