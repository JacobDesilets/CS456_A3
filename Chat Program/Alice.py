from socket import *
import ElGamal
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8081))
print('Connected.')

serverSock.listen(1)
connectionSock, addr = serverSock.accept()

# Create ElGamal Public Keys (p, g, b)
p, g, a, b = ElGamal.gen_keys(128)

# Send Public Keys to Bob (p, g, b)
sendStr = str(p) + ", " + str(g) + ", " + str(b)
connectionSock.send(sendStr.encode('utf-8'))
print('Sent the Public Keys to Bob')

# Receive Secret Keys from Bob
data = connectionSock.recv(1024)
ciphertext = pickle.loads(data)
AESKey = ElGamal.decrypt(ciphertext, p, a)
print('Decrypted AES key:', AESKey)

# Encrypt message by using AES secret keys and send it to Bob
message = input('Enter a message: ').encode('utf-8')
cipher = AES.new(pad(AESKey.encode('utf-8'), 16), AES.MODE_ECB)
encryptedMsg = cipher.encrypt(pad(message, 16))
connectionSock.send(encryptedMsg)
print('Sent the Encrypted Message to Bob')