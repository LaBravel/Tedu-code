def get_score() :
    try :
        a = int(input('输入成绩'))
    except ValueError as ve :
        print('程序出错',ve)
        return 0
    if a < 0 or a > 100 :
        return 0
    else :
        print('运行成功')
        return a


print('输入的成绩是',get_score())

