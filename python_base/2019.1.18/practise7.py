def get_age () :
    try :
        ages = int(input('输入年龄'))
    except :
        raise ValueError('输入数据无效')
    if not 1 <= ages <= 140 :
        raise ValueError('输入数据无效')
    return ages    

print('用户输入的年龄是',get_age())