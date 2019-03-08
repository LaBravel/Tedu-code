from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',1024))

#确定数据结构
st = struct.Struct('i16sf')

while True :
    data,addr = s.recvfrom(1024)
    data = st.unpack(data) #解析数据
    print(data)

s.close()