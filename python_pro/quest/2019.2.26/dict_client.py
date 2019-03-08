from socket import *
import sys
import getpass

#创建网络连接
def main() :
    if len(sys.argv) < 3 :
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    try :
        s.connect((HOST,PORT))
    except Exception as e :
        print(e)
        return
    
    while True :
        print('========Welcome========')
        print('-1.注册  -2.登录  -3.退出')
        print('=======================')

        try :
            cmd = int(input('输入选项:'))
        except Exception as e :
            print('请输入正确选项')
            continue
        if cmd == 1 :
            do_register(s)
        elif cmd == 2 :
            do_login(s)
        elif cmd == 3 :
            s.close()
            sys.exit()
        else :
            print('请输入正确选项')
            continue

def do_register(s) :
    while True :
        name = input('User:')
        passwd = getpass.getpass('请输入密码')
        passwd1 = getpass.getpass('请再次输入密码')
        if (' ' in name) or (' ' in passwd) :
            print('用户名与密码不许有空格')
            continue
        if passwd != passwd1 :
            print('两次密码输入不一致')
            continue
        msg = 'R %s %s' % (name,passwd)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == 'OK' :
            print('注册成功')
            login(s,name)
        elif data == 'EXISTS' :
            print('用户已存在')
        else :
            print('注册失败')

def do_login(s) :
    name = input('User:')
    passwd = getpass.getpass('请输入密码')
    msg = 'M %s %s' % (name,passwd)
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK' :
        print('登录成功')
        login(s,name)
    else :
        print('登录失败')        

def login(s,name) :
    while True :
        print('========Welcome========')
        print('-1.查词  -2.记录  -3.注销')
        print('=======================')

        try :
            cmd = int(input('输入选项:'))
        except Exception as e :
            print('请输入正确选项')
            continue
        if cmd == 1 :
            do_query(s,name)
        elif cmd == 2 :
            do_hist(s,name)
        elif cmd == 3 :
            return
        else :
            print('请输入正确选项')
            continue

def do_query(s,name) :
    while True :
        word = input('单词:')
        if word == '##' :
            break
        msg = 'Q %s %s' % (name,word)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        print(data)

def do_hist(s,name) :
    msg = 'H %s' % name
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK' :
        while True :
            data = s.recv(1024).decode()
            if data == '##' :
                break
            print(data)
    else :
        print('没有历史记录')

if __name__ == '__main__' :
    main()