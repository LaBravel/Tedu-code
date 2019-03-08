def get_score() :
    '''此函数强制用户输入０－１００之间的数，如果输入的
    是其他的数则直接触发异常来通知调用者'''
    score = int(input('请输入成绩'))
    if score < 0 :
        raise ValueError('成绩低于最小值')
    if score > 100 :
        raise ValueError('成绩超出最大值')
    return score

try :
    score = 0
    score = get_score()
except ValueError as err :
    print('用户输入有错，err = ',err)
print('学生成绩是',score)