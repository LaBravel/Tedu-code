import time,sys
print('设定系统时间')
h = int(input('h'))
m = int(input('m'))
while 1 :
    b = time.localtime()
    print('%02d:%02d:%02d' % b[3:6],end = '\r')
    if b[3] == h and b[4] == m :
        print('时间到！！')
        break
    time.sleep(1)
