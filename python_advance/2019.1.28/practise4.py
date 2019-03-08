try :
    with open('a.txt','rt') as f :
        for line in f :
            print(line)
    #with语句结束，文件自动关闭
except :
    print('文件操作失败')