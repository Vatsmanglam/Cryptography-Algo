from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return cipher.iv + ciphertext

def des_decrypt(ciphertext, key):
    iv = ciphertext[:DES.block_size]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[DES.block_size:]), DES.block_size)
    return plaintext.decode()

# Example usage
key = get_random_bytes(8)  # DES key (must be 8 bytes)
plaintext = "Hello DES Encryption"
ciphertext = des_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")
decrypted = des_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")
