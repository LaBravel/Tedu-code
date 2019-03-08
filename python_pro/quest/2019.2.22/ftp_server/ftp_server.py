from socket import *
import os,sys,signal,time

HOST= '0.0.0.0'
PORT = 1024
ADDR = (HOST,PORT)
file_path = './file_base/'
s = socket()
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

class FtpServer(object) :
    def __init__(self,c) :
        self.c = c
    
    def do_get(self) :
        fileslist = os.listdir(file_path)
        if not fileslist :
            self.c.send('文件库为空'.encode())
        else :
            self.c.send(b'OK')
            time.sleep(0.1)
        files = ''
        for filename in fileslist :
            if filename[0] != '.' and \
            os.path.isfile(file_path+filename) :
                files = files + filename + ','
        self.c.send(files.encode())
    
    def do_download(self,filename) :
        try :
            fd = open(file_path+filename,'rb')
        except IOError :
            print(filename)
            self.c.send('文件不存在'.encode())
            return
        else :
            self.c.send(b'OK')
            time.sleep(0.1)
        while True :
            data = fd.read(1024)
            if not data :
                time.sleep(0.1)
                self.c.send(b'##')
                print('下载完毕')
                break
            self.c.send(data)



def do_request(c) :
    ftp = FtpServer(c)
    while True :
        data = c.recv(1024).decode()
        if not data or data[0] == 'Q' :
            c.close()
            return
        elif data[0] == 'L' :
            ftp.do_get()
        elif data[0] == 'G' :
            filename = data.split(' ')[-1]
            ftp.do_download(filename)

def main() :
    while True :
        try :
            c,addr = s.accept()
            print('Connect to',addr)
        except KeyboardInterrupt :
            sys.exit('服务器退出')
            s.close()
        except Exception as e :
            print('Error:',e)
            continue
    
        pid = os.fork()
        if pid == 0 :
            s.close()
            do_request(c)
            os._exit(0)
        else :
            c.close()
            
if __name__ == '__main__' :
    main()
