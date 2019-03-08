fw = open('myflush.txt','w')
fw.write('hello')#此处执行的write操作没有真正写在磁盘上
fw.flush()
while 1 :
    pass
fw.close()