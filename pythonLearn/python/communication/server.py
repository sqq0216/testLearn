import socket, time
import threading

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定端口
s.bind(('127.0.0.1', 9999))
#监听端口，最多监听5个
s.listen(5)
print('等待连接')

def tcplink(sock, addr):
    print("从%s %s...接收新的连接：" % addr)
    sock.send(b'welcom')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
while True:
    #接受客户端的连接
    sock, addr = s.accept()
    print("sock is:", sock)
    print("and addr :", addr)
    #为一个client创建一个线程
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
s.close()
