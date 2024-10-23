import numpy as np

# Create a 5x5 Playfair matrix from the key
def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.replace("j", "i")))  # Remove duplicates, treat 'i' and 'j' as the same
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'j' is merged with 'i'
    key += "".join([char for char in alphabet if char not in key])  # Append remaining letters
    matrix = np.array(list(key)).reshape(5, 5)
    return matrix

# Get position of character in the 5x5 matrix
def find_position(matrix, char):
    row, col = np.where(matrix == char)
    return row[0], col[0]

# Prepare plaintext into digraphs with filler 'x' where needed
def prepare_text(plaintext):
    plaintext = plaintext.replace("j", "i").replace(" ", "")  # Normalize 'j' to 'i' and remove spaces
    digraphs = []
    i = 0
    while i < len(plaintext):
        # Create pairs of letters (digraphs)
        if i + 1 < len(plaintext) and plaintext[i] != plaintext[i + 1]:
            digraphs.append(plaintext[i:i+2])
            i += 2
        else:
            digraphs.append(plaintext[i] + 'x')  # Add 'x' if pair is the same or if it is a single letter left
            i += 1
    return digraphs

# Encrypt using Playfair cipher
def encrypt_playfair(plaintext, matrix):
    digraphs = prepare_text(plaintext)
    ciphertext = ""

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        # Rule 1: Same row -> shift right
        if row1 == row2:
            ciphertext += matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
        # Rule 2: Same column -> shift down
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
        # Rule 3: Rectangle -> swap columns
        else:
            ciphertext += matrix[row1, col2] + matrix[row2, col1]

    return ciphertext

# Decrypt using Playfair cipher
def decrypt_playfair(ciphertext, matrix):
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    decrypted_text = ""

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        # Rule 1: Same row -> shift left
        if row1 == row2:
            decrypted_text += matrix[row1, (col1 - 1) % 5] + matrix[row2, (col2 - 1) % 5]
        # Rule 2: Same column -> shift up
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5, col1] + matrix[(row2 - 1) % 5, col2]
        # Rule 3: Rectangle -> swap columns
        else:
            decrypted_text += matrix[row1, col2] + matrix[row2, col1]

    # Remove filler 'x' where necessary
    cleaned_text = ""
    i = 0
    while i < len(decrypted_text):
        # If 'x' was added between repeated letters, skip it during decryption
        if i < len(decrypted_text) - 1 and decrypted_text[i + 1] == 'x' and decrypted_text[i] == decrypted_text[i + 2]:
            cleaned_text += decrypted_text[i]
            i += 2  # Skip the 'x'
        else:
            cleaned_text += decrypted_text[i]
            i += 1

    return cleaned_text

# Example Usage
key = "playfairexample"
matrix = generate_playfair_matrix(key)
plaintext = "hidethegoldinthetreestump"
ciphertext = encrypt_playfair(plaintext, matrix)

print(f"Playfair Matrix:\n{matrix}")
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = decrypt_playfair(ciphertext, matrix)
print(f"Decrypted Text: {decrypted_text}")
