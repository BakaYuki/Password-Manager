from cryptography.fernet import Fernet

# Generate a key
# key = Fernet.generate_key()

# print(type(key))

#Location of key
# print(type(key))

# file = open("key.txt","r")
# a = file.read()
# print(a)
# x = bytes(a)
# print(type(x))
key = b'O0fbgOmTcPFKqWStK-o8VCigBF6vnm7OypaaRhh4p2U='
# Create a Fernet symmetric encryption object with the key
cipher_suite = Fernet(key)


# Message to be encrypted
message = "Hello, this is a secret message!"
print(type(message))
message1 = message.encode()
print(type(message1))
print(message1)
message2 = message1.decode()
print(message2)
# Encrypt the message
cipher_text = cipher_suite.encrypt(message1)

print("Encrypted message:", cipher_text)

# Decrypt the message
print(type(cipher_text))
plain_text = cipher_suite.decrypt(cipher_text)
# print("Decrypted message:",plain_text)
print("Decrypted message:", plain_text.decode())

m = 'gAAAAABmCVSTUYvyLr3MaOa2fSJR8iTd9oRVS1TKJGpgET7mfxa2T6kK0edEhhCks4qqamdCAdKX_vr4IstdrvkWJCQcZEIjQA=='
o = 'gAAAAABmCVTctnwqv4TqLoZ5tJYGzAuZ3-C5lHFDlTGQZv3DvMmIYJ-ibwfLLnzJTrkQZtejpgwEyS6gxqA447Pj9U_RfWg_Vlyq9Rwv4CLN0lj6x44pqgBC5V7d6TKhP2l5cbvZJq3p'
print(len(m))
print(len(plain_text))
print(len(cipher_text))