import math

def encrypt(plaintext, public_key):
    n, e = public_key
    ciphertext = pow(plaintext, e, n)

    return ciphertext

plaintext = 3264128256512 #set
public_key = (58979, 1) #n = 58979 d=<prev>

ciphertext = encrypt(plaintext, public_key)
print("Ciphertext:", ciphertext)