import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
class KerberosServer:
    def __init__(self):
        self.database = {}  # Simulating a database for user keys

    def register_user(self, username):
        key = os.urandom(16)  # Symmetric key for the user
        self.database[username] = key
        return key

    def generate_ticket(self, username, service_key):
        # Generate a session key and encrypt it with the user's key
        session_key = os.urandom(16)
        encrypted_session_key = self.encrypt_with_key(self.database[username], session_key)
        return session_key, encrypted_session_key

    def encrypt_with_key(self, key, data):
        cipher = AES.new(key, AES.MODE_CBC)
        return cipher.iv + cipher.encrypt(pad(data, AES.block_size))

    def decrypt_with_key(self, key, data):
        iv = data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)

# Example usage
server = KerberosServer()
user_key = server.register_user("Alice")
session_key, ticket = server.generate_ticket("Alice", user_key)
print(f"Session Key: {session_key}")
print(f"Encrypted Ticket: {ticket}")
