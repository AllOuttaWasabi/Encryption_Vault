from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

message = b"This will be signed"

key = RSA.generate(bits=1024)
hash = SHA256.new(message)

signature = pkcs1_15.new(key).sign(hash)

try:
    pkcs1_15.new(key).verify(hash, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature isn't valid.")