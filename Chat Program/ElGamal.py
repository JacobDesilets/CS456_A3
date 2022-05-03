import random

def miller_rabin(n, d):
    a = random.randint(2, n - 1)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False


def is_prime(n, k=6):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not miller_rabin(n, d):
            return False

    return True


def gen_p(nbits):
    while True:
        p = random.randint( 2**(nbits-2), 2**(nbits-1))
        if is_prime(p, k=10):
            return p


def gen_keys(bits):
    p = gen_p(bits)
    g = random.randint(3, p)
    a = random.randint(2, p)
    b = pow(g, a, p)

    return p, g, a, b


def encrypt(plaintext, p, g, b):
    ciphertext = []
    for i in range(0, len(plaintext)):
        alpha = random.randint(2, p)
        hmask = pow(g, alpha, p)
        fmask = pow(b, alpha, p)
        cipher = (fmask * ord(plaintext[i])) % p
        ciphertext.append((hmask, cipher))

    return ciphertext


def decrypt(ciphertext, p, a):
    plaintext = ''
    for line in ciphertext:
        hmask = line[0]
        cipher = line[1]
        f = pow(hmask, a, p)
        m = (pow(f, -1, p) * cipher) % p
        plaintext += chr(m)

    return plaintext

if __name__ == '__main__':
    # Testing
    p, g, a, b = gen_keys(128)

    message = 'This is a test of my ElGamal cryptosystem implementation'


    ciphertext = encrypt(message, p, g, b)
    print(ciphertext)
    plaintext = decrypt(ciphertext, p, a)


    print(plaintext)
