def fry_egg() :
    print('打开天然气...')
    try :    
        count = int(input('请输入鸡蛋个数'))
        print('完成煎蛋，共煎了%d个鸡蛋' % count)
    except ValueError :
        print('煎蛋过程中出错')
    finally :
        print('关闭天然气')

 
fry_egg()
