'''
Blake Jackson
Encrypting/Decrypting File Vault Assignment
CSC424
'''

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os
import time


def encrypt(fileName, i, type, newEncryptedFile):
    if type == "AES":
        type = AES.new
        type_MODE = AES.MODE_CBC
        blockSize = AES.block_size
    elif type == "DES":
        type = DES.new
        type_MODE = DES.MODE_CBC
        blockSize = DES.block_size
    elif type == "DES3":
        type = DES3.new
        type_MODE = DES3.MODE_CBC
        blockSize = DES3.block_size

    with open(fileName, 'rb') as f:
        data = f.read()

    data = pad(data, blockSize)

    with open(path + '\\aeskey', 'wb') as f:
        f.write(key)

    cipher = type(key, type_MODE)
    cipherText = cipher.encrypt(data)

    with open(newEncryptedFile + ".lol", 'wb') as f:
        f.write(cipher.iv)
        f.write(cipherText)


path = input("Enter the path of folder: ")
encryptionType = input("Enter in a type of encryption to use: (AES, DES, DES3)")

while (encryptionType != "AES") and (encryptionType != "DES") and (encryptionType != "DES3"):
    encryptionType = input("Enter a valid encryption type: AES, DES or DES3.")

vaultLocation = input("Enter the vault location to copy files: ")

list = os.listdir(path)

if encryptionType == "DES":
    key = get_random_bytes(8)
else:
    key = get_random_bytes(16)

counter = 0
for i in list:
    counter += 1
    fileName = path + "\\" + i
    print(fileName)
    newEncryptedFile = vaultLocation + "\\" + i
    startTime = time.perf_counter()
    encrypt(fileName, i, encryptionType, newEncryptedFile)
    endTime = time.perf_counter()
    print(counter, "\t", endTime - startTime)
