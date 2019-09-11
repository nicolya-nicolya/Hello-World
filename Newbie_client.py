import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
msg = input()
sock.send(msg.encode())

data = sock.recv(1024).decode()
sock.close()

print (data)