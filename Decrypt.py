'''
Blake Jackson
Encrypting/Decrypting File Vault Assignment
CSC424
'''

from Crypto.Cipher import  AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
import os
import time

def decrypt(fileName, type, keyLocation):
    with open(fileName, 'rb') as f:
        if (type == "DES3") or (type == "DES"):
            iv = f.read(8)
        else:
            iv = f.read(16)
        cipherText = f.read()

    with open(keyLocation, 'rb') as f:
        key = f.read()

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

    cipher = type(key, type_MODE, iv)

    data = cipher.decrypt(cipherText)
    data = unpad(data, blockSize)

    with open(fileName[:-4], 'wb') as f:
        f.write(data)


path = input("Enter the path of folder: ")

encryptionType = input("Enter in a type of encryption to use: (AES, DES, DES3)")

while (encryptionType != "AES") and (encryptionType != "DES") and (encryptionType != "DES3"):
    encryptionType = input("Enter a valid encryption type: AES, DES or DES3.")

keyLocation = input("Enter the location of the key: ")
keyLocation = keyLocation + "\\aeskey"

list = os.listdir(path)
counter = 0
for i in list:
    counter += 1
    fileName = path + "\\" + i
    #encrypt(fileName, i)
    startTime = time.perf_counter()
    decrypt(fileName, encryptionType, keyLocation)
    endTime = time.perf_counter()
    print(counter, "\t", endTime - startTime)