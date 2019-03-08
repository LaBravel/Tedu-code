try :
    f = open('myfile.txt')
    print('文件打开成功')
    s = f.read()
    print('读取字符的个数是',len(s))
    print('文件的内容是','\n',s,sep = '')
    f.close
    print('文件关闭成功')
except OSError :
    print('文件打开失败')