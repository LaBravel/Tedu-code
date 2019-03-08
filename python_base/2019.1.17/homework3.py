def input_student() :
    while 1 :
        name = input("请输入姓名(按回车返回上一级)")
        if name == '' :
            break
        Ages = input("请输入年龄")   
        # if Ages <= '0' or Ages >= '999' :
        #     print('输入信息无效!请重新输入')
        #     continue
        Scores = input("请输入成绩")
        # if Scores < '0' or Scores > '9' :
        #     print('输入信息无效!请重新输入')
        #     continue        
        D = {'姓名':name,'年龄':Ages,'成绩':Scores}
        DATE.append(D)

def output_student(DATE) :
    j = 1 
    if DATE == [] :
        width_name = 8
    else :
        width_name = max([len(i['姓名']) for i in DATE]) + 4
    print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    print('|','No'.center(4),'|','Name'.center(width_name),'|','Ages'.center(8) ,'|','Scores'.center(8),'|',sep = ''),
    print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    for i in DATE :
        print('|',('%-2d' % j).center(4),'|',i['姓名'].center(width_name),'|',i['年龄'].center(8) ,'|',i['成绩'].center(8),'|',sep = '')
        j += 1
    if DATE == [] :
        print('|',''.center(4),'|',''.center(width_name),'|',''.center(8) ,'|',''.center(8),'|',sep = '')
    print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')

def delete_student(DATE) :
    if DATE == [] :
        print('请先输入数据！')
        return
    while 1 :    
        output_student(DATE)
        choice_delete0 = input('输入要删除信息的学生编号(按回车返回上一级)')
        if choice_delete0 == '' :
            break
        elif choice_delete0 <= '0' or choice_delete0 >= '99999' :
            print('输入编号无效！请重新输入')
            continue
        choice_delete = int(choice_delete0) - 1
        if choice_delete + 1 > len(DATE) :
            print('输入编号无效！请重新输入')
            continue
        print('确定要删除',DATE[choice_delete],'吗？')
        confirm = input('按１确定，否则取消')
        if confirm == '1' :
            DATE.pop(choice_delete)
        if DATE == [] :
            print('已删除所有数据!')
            break

def edit_student(DATE) :
    if DATE == [] :
        print('请先输入数据！')
        return    
    while 1 :    
        output_student(DATE)
        edit_delete = input('输入要删除信息的学生编号(按回车返回上一级)')
        if edit_delete == '' :
            break
        edit_delete1 = int(edit_delete) - 1
        print('要修改',DATE[edit_delete1],'中的哪一项？')
        edit_delete2 = 1
        while edit_delete2 :
            output_student(DATE)
            edit_delete2 = input('修改哪一项？　1)姓名  2)年龄  3)成绩  其它)返回上一级')
            if edit_delete2 == '1' :
                NewName = input("输入新的姓名")
                DATE[edit_delete1]['姓名'] = NewName
            elif edit_delete2 == '2' :
                NewAges = input("输入新的年龄")
                DATE[edit_delete1]['年龄'] = NewAges
            elif edit_delete2 == '3' :
                NewScores = input("输入新的成绩")
                DATE[edit_delete1]['成绩'] = NewScores
            else :
                edit_delete2 = False

def sorted_scores_student(DATE,order) :
    if DATE == [] :
        print('请先输入数据！')
        return    
    DATE_sorted_scores = sorted(DATE,key = lambda x : x['成绩'],reverse = order)
    output_student(DATE_sorted_scores)

def sorted_ages_student(DATE,order) :
    if DATE == [] :
        print('请先输入数据！')
        return    
    DATE_sorted_ages = sorted(DATE,key = lambda x : x['年龄'],reverse = order)
    output_student(DATE_sorted_ages) 

def show_menu() :
        print('+','-' * 24,'+',sep = '')
        print('|','1) 添加学生信息'.center(18),'|',sep = '')
        print('|','2) 显示学生信息'.center(18),'|',sep = '')
        print('|','3) 删除学生信息'.center(18),'|',sep = '')
        print('|','4) 修改学生信息'.center(18),'|',sep = '')
        print('|','5) 按成绩降序排列'.center(17),'|',sep = '')
        print('|','6) 按成绩升序排列'.center(17),'|',sep = '')
        print('|','7) 按年龄降序排列'.center(17),'|',sep = '')
        print('|','8) 按年龄升序排列'.center(17),'|',sep = '')
        print('|','Q) 结束程序　　 '.center(18),'|',sep = '')
        print('+','-' * 24,'+',sep = '')
        
def main() :
    while 1 :
        show_menu()
        choice = input('要进行什么操作？')
        if choice == '1' :
            input_student()
        elif choice == '2' :
            output_student(DATE)
        elif choice == '3' :
            delete_student(DATE)
        elif choice == '4' :
            edit_student(DATE)
        elif choice == '5' :
            sorted_scores_student(DATE,True)
        elif choice == '6' :
            sorted_scores_student(DATE,False)
        elif choice == '7' :
            sorted_ages_student(DATE,True)
        elif choice == '8' :
            sorted_ages_student(DATE,False)
        elif choice == 'q' or choice == 'Q' :
            break
        else :
            print('没有这项操作！')

DATE = []
main()

