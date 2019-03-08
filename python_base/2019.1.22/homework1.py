a = input('输入源文件名称')
b = input('输入目标文件名称')
try :
    try :
        files = open(a,'rb')
        try :
            copy = open(b,'wb')
            while 1 :
                paste = files.read(4096)
                if not paste :
                    print('导入完毕')
                    break
            copy.write(paste)
        finally :
            copy.close()
    finally :
        files.close()
    print('复制成功！')
except OSError :
    print('复制失败！')
     



