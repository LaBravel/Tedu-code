def input_student(DATE) :
    while 1 :
        name = input("请输入姓名(按回车返回上一级)")
        if name == '' :
            break
        try :
            Ages = int(input("请输入年龄"))
            if not 0 < Ages < 140 :
                raise ZeroDivisionError 
            Scores = float(input("请输入成绩"))
            if not 0 < Scores < 100 :
                raise ZeroDivisionError             
        except ValueError :
            print('输入信息无效，请重新输入')
            continue     
        except ZeroDivisionError :
            print('输入信息不在规定范围内，请重新输入')
            continue 
        D = {'姓名':name,'年龄':Ages,'成绩':Scores}
        DATE.append(D)

def output_student(DATE) :
    j = 1 
    try :
        width_name = max([len(i['姓名']) for i in DATE]) + 4
    except ValueError :
        width_name = 8
    print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    print('|','No'.center(4),'|','Name'.center(width_name),'|','Ages'.center(8) ,'|','Scores'.center(8),'|',sep = ''),
    print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
    for i in DATE :
        print('|',('%-2d' % j).center(4),'|',i['姓名'].center(width_name),'|',('%d' % i['年龄']).center(8) ,'|',('%d' % i['成绩']).center(8),'|',sep = '')
        print('+','-' * 4,'+','-' * width_name,'+','-' * 8,'+','-' * 8,'+',sep = '')
        j += 1

def delete_student(DATE) :
    while 1 :    
        try :
            output_student(DATE)
            choice_delete0 = input('输入要删除信息的学生编号(按回车返回上一级)')
            if choice_delete0 == '' :
                break
            choice_delete = int(choice_delete0) - 1
            print('确定要删除',DATE[choice_delete],'吗？')
            confirm = input('按１确定，否则取消')
            if confirm == '1' :
                DATE.pop(choice_delete)
            if DATE == [] :
                print('已删除所有数据!')
                break
        except ValueError :
            print('输入信息无效，请重新输入')
            continue
        except IndexError :
            print('列表中没有此项数据,请重新输入')
            continue
        
def edit_student(DATE) :
    while 1 :    
        output_student(DATE)
        try :    
            edit_delete = input('输入要修改信息的学生编号(按回车返回上一级)')
            if edit_delete == '' :
                break
            edit_delete = int(edit_delete) - 1
            print('要修改',DATE[edit_delete],'中的哪一项？')
        except ValueError :
            print('输入信息无效，请重新输入')
            continue
        except IndexError :
            print('列表中没有此项数据,请重新输入')
            continue
        edit_delete2 = 1
        while edit_delete2 :
            output_student(DATE)
            edit_delete2 = input('修改哪一项？　1)姓名  2)年龄  3)成绩  其它)返回上一级')
            if edit_delete2 == '1' :
                NewName = input("输入新的姓名")
                DATE[edit_delete]['姓名'] = NewName
            elif edit_delete2 == '2' :
                try :
                    NewAges = int(input("输入新的年龄"))
                    if not 0 < NewAges < 140 :
                        print('输入信息不在规定范围内，请重新输入')
                        continue
                    DATE[edit_delete]['年龄'] = NewAges
                except ValueError :
                    print('输入信息无效，请重新输入')
                    continue
            elif edit_delete2 == '3' :
                try :
                    NewScores = int(input("输入新的成绩"))
                    if not 0 <= NewScores <= 100 :
                        print('输入信息不在规定范围内，请重新输入')
                        continue
                    DATE[edit_delete]['成绩'] = NewScores
                except ValueError :
                    print('输入信息无效，请重新输入')
                    continue
            else :
                edit_delete2 = False

def sorted_scores_student(DATE,order) :
    DATE_sorted_scores = sorted(DATE,key = lambda x : x['成绩'],reverse = order)
    output_student(DATE_sorted_scores)

def sorted_ages_student(DATE,order) :
    DATE_sorted_ages = sorted(DATE,key = lambda x : x['年龄'],reverse = order)
    output_student(DATE_sorted_ages) 

def load_info_student(DATE) :
    while 1 :    
        try :
            a = input('输入要打开的文件名,按回车返回上一级')
            if a == '' :
                break
            files = open(a)
            load_files = files.readlines()
            print('确定加入以下数据吗?')
            for i in load_files :
                name,ages,scores = i.split(',')
                print('姓名:%s,年龄:%s,成绩:%s' % (name,ages,scores))
            b = input('按1确认，否则取消')
            if b != '1' :
                continue
            for i in load_files :
                name,ages,scores = i.split(',')
                D = {'姓名':name,'年龄':int(ages),'成绩':int(scores)}
                DATE.append(D)
            files.close
            output_student(DATE)
        except OSError :
            print('文件不存在，请重新输入')
            continue
        except ValueError :
            print('文件中数据不符合输入标准,请重新输入')
            continue

def save_info_student(DATE) :
    while 1 :
        output_student(DATE)
        try :
            a = input('输入文件名称,按回车返回上一级')
            if a == '' :
                break
            info = open(a,'x')
            for i in DATE :
                info.write('%s,%d,%d\n' % (i['姓名'],i['年龄'],i['成绩']))
            info.close
            print('保存',a,'成功')
            break
        except FileExistsError :
            print('文件名已存在，是否覆盖原文件?')
            b = input('按１确认覆盖，其它取消')
            if b == '1' :
                info = open(a,'w')
            else :
                continue
            for i in DATE :
                info.write('%s,%d,%d\n' % (i['姓名'],i['年龄'],i['成绩']))
            info.close
            print('保存',a,'成功')
            break

