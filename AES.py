#Python 3.10.2
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def encrypt(plain_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    plain_text = pad(plain_text)
    print("After padding:", plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text))
message=input("Enter message to encrypt: ");
key = input("Enter encryption key: ")
encrypted_msg = encrypt(message, key)
print("Encrypted Message:", encrypted_msg)

