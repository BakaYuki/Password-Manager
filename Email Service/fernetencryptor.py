from cryptography.fernet import Fernet

#For Encryption and Decryption Using Fernet
KEY = b'O0fbgOmTcPFKqWStK-o8VCigBF6vnm7OypaaRhh4p2U='
encryptor = Fernet(KEY)

# Function to encrypt data
def encrypt_data(data):
    return encryptor.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data):
    return encryptor.decrypt(encrypted_data).decode()
