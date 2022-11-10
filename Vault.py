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

    data = pad(data, AES.block_size)
    key = get_random_bytes(16)

    with open('pg64330-images.epub', 'wb') as f:
        f.write(key)

    cipher = AES.new(key, AES.MODE_CBC)
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

    keyLocation = input("Enter the location of the key: ")
    with open(keyLocation + '\\aeskey', 'rb') as f:
        key = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(cipherText)
    data = unpad(data, AES.block_size)

    with open(fileName[:-4], 'wb') as f:
        f.write(data)

for i in list:
    fileName = path + "\\" + i
    print(fileName)

    #encrypt(fileName, i)
    decrypt(fileName)











