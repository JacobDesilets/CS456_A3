from socket import *
import ElGamal
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8081))

print('Bob Connected.')

# Receive Public Key from Alice (p, g, b)
data = clientSock.recv(1024).decode('utf-8')
publicKeys = data.split(", ")
p = int(publicKeys[0])
g = int(publicKeys[1])
b = int(publicKeys[2])
print('Received Public Keys')
print('p:', p)
print('g:', g)
print('b:', b)

# Create Secret Keys and encrypt it by using Public Keys
AESKey = input("Enter AES key: ")
cipherText = ElGamal.encrypt(AESKey, p, g, b)

# Send Encrypted Secret Keys to Alice
clientSock.send(pickle.dumps(cipherText))
print('Sent the Secret Keys to Alice.')

# Receive Encrypted message from Alice
encryptedMsg = clientSock.recv(1024)
print('Received Encrypted Message')
print(encryptedMsg)

# Decrypt the Encrypted message using AES secret keys
cipher = AES.new(pad(AESKey.encode('utf-8'), 16), AES.MODE_ECB)
decryptedMsg = cipher.decrypt(encryptedMsg)
unpadMsg = unpad(decryptedMsg, 16)
print('Decrypted Message')
print(unpadMsg.decode('utf-8'))