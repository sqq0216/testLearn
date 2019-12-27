import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
# b 表示字符串为byte类型
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
#print(data)
# 1表示分割一次，即最后分为两个元素
header, html = data.split(b'\r\n\r\n', 1)
#print("date  split is :", data.split(b'\r\n\r\n', 1))
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('D:\\TestProjects\\testLearn\\doc\\python\\communication\\sina.html', 'wb') as f:
    f.write(html)