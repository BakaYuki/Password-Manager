#For Encryption and Decryption using Ceaser Cipher
s = 5
def ceaserencrypt(m):
    encrypted = ''
    for i in range(len(m)):
        e += chr(ord(m[i]) + s)
        encrypted.append(e)
    return encrypted

def ceaserdecrypt(m):
    decrypted = ''
    for i in range(len(m)):
        d += chr(ord(m[i]) - s)
        decrypted.append(d)
    return decrypted
