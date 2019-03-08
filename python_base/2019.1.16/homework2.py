# import time
# # a = time.strftime('%X')
# # print(a)

def show_time():
    import time
    while 1 :
        t = time.localtime()
        print('%02d:%02d:%02d' % t[3 : 6],end = '\r')
        time.sleep(1)
show_time()