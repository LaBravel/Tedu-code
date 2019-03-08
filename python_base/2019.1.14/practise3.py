i = 0
def fx() :
    global i
    i += 1
    print('第',i,'次调用')
while i <= 99 :
    fx()    