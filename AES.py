from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode()

# Example usage
key = get_random_bytes(16)  # AES-128
plaintext = "Hello AES Encryption"
ciphertext = aes_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")
decrypted = aes_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")
