"""
客户端
"""
from socket import*
# 创建tcp套接字
s = socket()
# 连接服务端程序
s.connect(('127.0.0.1',8899))
# 发送接收消息
while True:
    mag = input("msg>>")
    if not mag:
        break
    s.send(mag.encode())
    me = s.recv(1024)
    print("Server:",me)
s.close()
