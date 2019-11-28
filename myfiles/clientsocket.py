import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.1.0.0',12345))
print(s.recv(1024).decode())

while True:
    pass
