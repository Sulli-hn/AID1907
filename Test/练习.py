"""
tcp套接字服务端功能流程
"""
import socket
# 创建TCP套接字
sockft = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# 绑定地址
sockft.bind(('127.0.0.1',8899))
# 设置监听
sockft.listen(5)
# 阻塞等待客户端连接
print("Waiting for connect...")
connfd,addr = sockft.accept()
# 消息收发
while True:
    data = connfd.recv(1024)
    if not data:
        break
    print(data.decode())
    n = connfd.send(b"Thanks")
    print("Send %d bytes"%n)
connfd.close()
sockft.close()