import random
from math import gcd

def gen_p(nbits):
    while True:
        p = random.randint( 2**(nbits-2), 2**(nbits-1))
        if p % 2 == 0:
            continue

        for i in range(2, p // 2 + 1):
            if p % i == 0:
                continue

        return p

def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key

def gen_keys():
    p = gen_p(8)
    g = random.randint(2, p)
    a = random.randint(1, (p-1) // 2)
    
    b = pow(g, a, p)

    return p, g, a, b


def encrypt(txt, p, g, a):
    alpha = random.randint(1, p)
    hmask = pow(g, alpha, p)
    fmask = pow(hmask, a, p)
    
    ciphertext = []
    for i in range(0, len(txt)):
        ciphertext.append((hmask, (fmask * ord(txt[i])) % p))

    return ciphertext


def decrypt(h, c, a, p):
    return (pow(pow(h, a, p), -1, p) * c) % p


p, g, a, b = gen_keys()

txt = 'This is a test'
plaintxt = ''

ciphertext = encrypt(txt, p, g, a)
for h, c in ciphertext:
    plaintxt += chr(decrypt(h, c, a, p))

print(plaintxt)
