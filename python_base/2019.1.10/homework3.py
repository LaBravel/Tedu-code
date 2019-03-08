def input_student() :
    DATE = []
    while 1 :
        name = input("请输入姓名")
        if name == '' :
            return DATE
        Ages = input("请输入年龄")
        Scores = input("请输入成绩")
        D = {'姓名':name,'年龄':Ages,'成绩':Scores}
        DATE.append(D)
def output_student(DATE) :
    width_name = max([len(i['姓名']) for i in DATE]) + 4
    print('+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    print('|','Name'.center(width_name),'|','Ages'.center(8) ,'|','Scores'.center(8),'|',sep = ''),
    print('+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    for i in DATE :
        print('|',i['姓名'].center(width_name),'|',i['年龄'].center(8) ,'|',i['成绩'].center(8),'|',sep = '')
    print('+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
DATE = input_student()
print(DATE)
output_student(DATE)
