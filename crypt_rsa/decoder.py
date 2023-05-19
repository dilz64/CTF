import math

def decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext = pow(ciphertext, d, n)

    return plaintext

ciphertext = 24538 #set
private_key = (58979, 1) #n = 58979 d=<prev>

plaintext = decrypt(ciphertext, private_key)
print("Plaintext:", plaintext)