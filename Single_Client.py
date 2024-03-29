import socket
s = socket.socket()
port = 6969
s.connect(('127.0.0.1', port))
while True:
    print(s.recv(1024).decode())
    message=(input('Enter: '))
    if(message == 'quit'):
       break
    s.send(message.encode())
s.close()
