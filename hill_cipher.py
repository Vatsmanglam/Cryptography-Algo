import numpy as np
from sympy import Matrix  # Using sympy for modular matrix inversion

# Convert a letter to its position in the alphabet (0 for 'a', 1 for 'b', ..., 25 for 'z')
def letter_to_number(letter):
    return ord(letter) - ord('a')

# Convert a number (0-25) back to a letter
def number_to_letter(number):
    return chr(number + ord('a'))

# Encrypt a block of text using the Hill cipher
def encrypt_hill(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").lower()

    # Ensure the length of plaintext is a multiple of the matrix size (padding if needed)
    n = key_matrix.shape[0]
    if len(plaintext) % n != 0:
        plaintext += 'x' * (n - (len(plaintext) % n))  # Padding with 'x'

    # Convert the plaintext into numbers
    plaintext_vector = [letter_to_number(c) for c in plaintext]
    ciphertext = ""

    # Divide the plaintext into blocks and multiply each by the key matrix
    for i in range(0, len(plaintext_vector), n):
        block = np.array(plaintext_vector[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(number_to_letter(num) for num in encrypted_block)

    return ciphertext

# Decrypt a block of ciphertext using the Hill cipher
def decrypt_hill(ciphertext, key_matrix):
    n = key_matrix.shape[0]

    # Use sympy to find the modular inverse of the key matrix
    key_matrix_mod_inv = Matrix(key_matrix).inv_mod(26)
    inverse_key_matrix = np.array(key_matrix_mod_inv).astype(int)

    # Convert ciphertext into numbers
    ciphertext_vector = [letter_to_number(c) for c in ciphertext]
    decrypted_text = ""

    # Divide the ciphertext into blocks and multiply each by the inverse key matrix
    for i in range(0, len(ciphertext_vector), n):
        block = np.array(ciphertext_vector[i:i+n])
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        decrypted_text += ''.join(number_to_letter(num) for num in decrypted_block)

    return decrypted_text

# Example Usage
# Key matrix (3x3 example)
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

plaintext = "helpmeobiwankenobi"
ciphertext = encrypt_hill(plaintext, key_matrix)

print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = decrypt_hill(ciphertext, key_matrix)
print(f"Decrypted Text: {decrypted_text}")
