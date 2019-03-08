i = 2
while i >= 0 :
    a = input("请输入用户名")#用户名suxiao
    b = input("请输入密码")#密码123456
    if a == 'suxiao' and b == '123456' :
        print("登录成功！")
        i -= 99999999
    else :
        print("用户名或密码错误，请再试一次！",'\n','还有',i,"次机会",sep = '')
        i -= 1
else :
    pass
    
