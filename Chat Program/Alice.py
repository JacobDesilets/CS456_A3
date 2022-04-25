from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr), 'has connected.')

data = connectionSock.recv(1024)
print('Data from Bob:', data.decode('utf-8'))

connectionSock.send('I am Alice.'.encode('utf-8'))
print('Sent a message to Bob')