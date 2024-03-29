import socket
s = socket.socket()
print('Socket created')
port = 6969
s.bind(('', port))
print(f'Socket successfully binded to port {port}')
s.listen(10)
print("Socket is listening")
c, addr = s.accept()
print('Address connection aquired')
message = ('You have connected!')
c.send(message.encode())
while True:
    print(c.recv(1024).decode())
    message=(input('Enter: '))
    if(message == 'quit'):
       break
    c.send(message.encode())

c.close()
