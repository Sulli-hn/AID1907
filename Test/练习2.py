"""
udp_server.py
"""
from socket import *
# 创建数据报套接字
sockft = socket(AF_INET,SOCK_DGRAM)
# 绑定地址
sockft.bind(('127.0.0.1',8888))
# 循环消息收发
while True:
    data,addr = sockft.recvfrom(1024)
    print("收到消息:",data.decode())
    n = sockft.sendto(b'Thanks',addr)
sockft.close()