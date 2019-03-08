from socket import *
import os,sys,time

s = socket()
class FtpClient(object) :
    def __init__(self,s) :
        self.s = s
    
    def do_get(self) :
        self.s.send(b'L ')
        data = self.s.recv(1024).decode()
        if data == 'OK' :
            data = self.s.recv(4096).decode()
            files = data.split(',')
            for i in files :
                print(i)
        else :
            print(data) #打印为何无法完成
    def do_download(self,filename) :
        self.s.send(('G '+filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'OK' :
            fd = open(filename,'wb')
            while True :
                data = self.s.recv(1024)
                if data == b'##' :
                    break
                fd.write(data)
            fd.close()
        else :
            print(data)
    def do_updata(self,filename) :
        try :
            f = open(filename,'rb')
        except IOError :
            print('没有该文件')
            return
        filename = filename.split('/')[-1]
        self.s.send(('P '+filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'OK' :
            while True :
                data = f.read(1024)
                if not data :
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
        else :
            print(data)
    def do_exit(self) :
        self.s.send(b'Q ')
        self.s.close()
        sys.exit('谢谢使用')
    

def main() :
    try :
        s.connect(('127.0.0.1',1024))
    except Exception as e :
        print('Error:',e)
        return
    ftp = FtpClient(s)
    while True :
        print('\n========M E N U========')
        print('\n========getlist========')
        print('\n========download=======')
        print('\n========update=========')
        print('\n========E X I T========')
        
        cmd = input('>>>')

        if cmd.strip() == 'get' :
            ftp.do_get()
        elif cmd.strip()[:8] == 'download' :
            filename = cmd.split(' ')[-1]
            ftp.do_download(filename)
        elif cmd.strip() == 'updata' :
            filename = cmd.split(' ')[-1]
            ftp.do_updata(filename)
        elif cmd.strip() == 'exit' :
            ftp.do_exit()
        else :
            print('Orders incorrcet')

if __name__ == '__main__' :
    main()