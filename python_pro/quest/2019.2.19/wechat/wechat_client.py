from socket import *
import os,sys

#服务器地址
ADDR = ('127.0.0.1',1024)

def send_msg(s,name) :
    while True :
        text = input('发送:')
        if text == 'quit' :
            msg = 'Q %s %s' % (name,text)
            s.sendto(msg.encode(),ADDR)
            os._exit(1)
            break
        else :    
            msg = 'C %s %s' % (name,text)
            s.sendto(msg.encode(),ADDR)

def recv_msg(s) :
    while True :
        data,addr = s.recvfrom(2048)
        print(data.decode())
        if data.decode() == 'Unconnect Succeed' :
            os._exit(1)
            break    
#创建网络连接
def main() :
    s = socket(AF_INET,SOCK_DGRAM)
    
    while True :
        name = input('请输入姓名')
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)#等待回应
        if data.decode() == 'OK' :
            print('进入聊天室')
            break
        else :
            print(data.decode())
    #创建新的进程
    pid = os.fork()
    if pid < 0 :
        sys.exit('Error!')
    elif pid == 0 :
        send_msg(s,name)
    else :
        recv_msg(s)

if __name__ == '__main__' :
    main()