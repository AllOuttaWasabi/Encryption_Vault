from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

import os



path = input("Enter the path of folder: ")

list = os.listdir(path)

def encrypt(fileName, i):
    with open(fileName, 'rb') as f:
        data = f.read()

    data = pad(data)
    key = get_random_bytes(16)

    with open(path + '\\aeskey', 'wb') as f:
        f.write(key)

    cipher = AES.new(key,AES.MODE_CBC)
    cipherText = cipher.encrypt(data)

    vaultLocation = input("Enter the vault location to copy files: ")
    newEncryptedFile = vaultLocation + "\\" + i

    with open(newEncryptedFile + ".lol", 'wb') as f:
        f.write(cipher.iv)
        f.write(cipherText)


def decrypt(fileName):
    with open(fileName, 'rb') as f:
        iv = f.read(16)
        cipherText = f.read()

    with open(path + '\\aeskey', 'wb') as f:
        key

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(cipherText), AES.block_size)
    print(data)

for i in list:
    fileName = path + "\\" + i
    print(fileName)

    #encrypt(fileName, i)
    decrypt(fileName)








