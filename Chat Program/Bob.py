from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('Connected.')
clientSock.send('I am Bob.'.encode('utf-8'))

print('Sent a message to Alice.')

data = clientSock.recv(1024)
print('Data from Alice:', data.decode('utf-8'))