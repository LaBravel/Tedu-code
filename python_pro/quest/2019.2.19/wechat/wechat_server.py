'''
chatroom
env: python3.5
exc: socket and fork
'''
from socket import *
import os,sys
user = {}

def do_login(s,name,addr) :
    if name in user :
        s.sendto('该用户已存在'.encode(),addr)
        return
    else :
        s.sendto(b'OK',addr)
    msg = '欢迎%s来到聊天室' % name
    for i in user :
        s.sendto(msg.encode(),user[i])
    user[name] = addr

def do_chat(s,name,text) :
    msg = '%s : %s' % (name,text)
    for i in user :
        if i != name :
            s.sendto(msg.encode(),user[i])

def do_quit(s,name,addr) :
    msg = '%s已经退出聊天室' % name
    del user[name]
    s.sendto(b'Unconnect Succeed',addr)
    for i in user :
        s.sendto(msg.encode(),user[i])

def do_requests(s) :
    while True :
        data,addr = s.recvfrom(1024)
        msglist = data.decode().split(' ')
        if msglist[0] == 'L' :
            do_login(s,msglist[1],addr)
        elif msglist[0] == 'C' :
            text = ' '.join(msglist[2:])
            do_chat(s,msglist[1],text)
        elif msglist[0] == 'Q' :
            do_quit(s,msglist[1],addr)


#创建网络连接
def main() :
    ADDR = ('0.0.0.0',1024)
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    

    #创建单独进程用于发送管理员消息
    pid = os.fork()
    if pid < 0 :
        print('Error')
        return
    elif pid == 0 :
        while True :
            msg = input('管理员消息')
            msg = 'C 管理员消息' + msg
            s.sendto(msg.encode(),ADDR)
    else :
        do_requests(s) #处理各种客户端需求

if __name__ == '__main__' :
    main()