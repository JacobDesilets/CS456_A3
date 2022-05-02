from socket import *
from Crypto.Cipher import AES

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('Connected.')

# Receive Public Key from Alice (p, g, b)
data = clientSock.recv(1024).decode('utf-8')
print(data)
print('Public Key:', data)

# Create Secret Keys using AES (not yet)
publicKeys = data.split(", ")
message = "p: " + publicKeys[0] + ", g: " + publicKeys[1] + ", b: " + publicKeys[2]
print(message)


# Send Secret Keys to Alice
clientSock.send('(?, ?)'.encode('utf-8'))
print('Sent the Secret Keys to Alice.')