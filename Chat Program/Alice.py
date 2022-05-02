from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print('Bob', str(addr), 'has connected.')

p = 7  # public key
g = 3  # public key
a = 5  # secret key
b = pow(g, a, p)  # public key (b = g^a mod p)

# Send Public Keys to Bob (p, g, b)
sendStr = str(p) + ", " + str(g) + ", " + str(b)
connectionSock.send(sendStr.encode('utf-8'))
print('Sent the Public Keys to Bob')

# Receive Secret Keys from Bob
data = connectionSock.recv(1024)
print('Secret Key:', data.decode('utf-8'))
