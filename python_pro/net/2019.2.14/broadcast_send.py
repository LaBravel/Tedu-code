from socket import *
from time import sleep

#目标地址
dest = ('172.40.71.255',1024)
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = '''
办证130xxxxxxxx
'''
while True :
    sleep(2)
    s.sendto(data.encode(),dest)

s.close()