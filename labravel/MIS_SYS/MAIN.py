from MENU import *
from STUDENT import *
def main():
    DATE = []
    while 1 :
        show_menu()
        choice = input('要进行什么操作？')
        if choice == '1' :
            input_student(DATE)
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
        elif choice == '9' :
            load_info_student(DATE)
        elif choice == '10' :
            save_info_student(DATE)
        elif choice == 'q' or choice == 'Q' :
            break
        else :
            print('没有这项操作！')

main()
