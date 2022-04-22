# pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
from base64 import b64encode

from helper import path_to_file

PUBLIC_KEY_PATH = path_to_file('public_key.pem')
PRIVATE_KEY_PATH = path_to_file('private_key.pem')


class Cryptography:
    @staticmethod
    def encrypt(data):
        with open(PUBLIC_KEY_PATH, "rb") as file:
            public_key = RSA.importKey(file.read())

        encryptor = PKCS1_OAEP.new(public_key)
        return b64encode(encryptor.encrypt(data.encode())).decode()

    @staticmethod
    def decrypt(data):
        with open(PRIVATE_KEY_PATH, "rb") as file:
            private_key = RSA.importKey(file.read())

        decryptor = PKCS1_OAEP.new(private_key)
        return decryptor.decrypt(b64decode(data)).decode()


if __name__ == '__main__':
    message = "text to be encrypted"
    encrypted = Cryptography.encrypt(message)
    print(encrypted)

    decrypted = Cryptography.decrypt(encrypted)
    print(decrypted)
