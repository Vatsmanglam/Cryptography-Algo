import string
import random

# Generate a random substitution alphabet
def generate_substitution_alphabet():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]  # Copy the original alphabet
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

# Monoalphabetic encryption function
def encrypt_monoalphabetic(plaintext, substitution_alphabet):
    result = ""
    for char in plaintext.lower():
        if char in substitution_alphabet:
            result += substitution_alphabet[char]
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

# Monoalphabetic decryption function
def decrypt_monoalphabetic(ciphertext, substitution_alphabet):
    reverse_alphabet = {v: k for k, v in substitution_alphabet.items()}  # Reverse the mapping
    print(f"Reverse Alphabet: {reverse_alphabet}")
    result = ""
    for char in ciphertext:
        if char in reverse_alphabet:
            result += reverse_alphabet[char]
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result


# Example Usage
substitution_alphabet = generate_substitution_alphabet()
# plaintext = "hello world"
plaintext = str(input())
ciphertext = encrypt_monoalphabetic(plaintext, substitution_alphabet)

print(f"Substitution Alphabet: {substitution_alphabet}")
print(f"Ciphertext: {ciphertext}")

# Example Usage
decrypted_text = decrypt_monoalphabetic(ciphertext, substitution_alphabet)
print(f"Decrypted Text: {decrypted_text}")


