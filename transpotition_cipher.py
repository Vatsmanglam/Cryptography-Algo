def encrypt_transposition(plaintext, key):
    # Create a list to hold the columns
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols  # Round up division
    padded_length = num_rows * num_cols
    
    # Pad the plaintext with spaces to fill the grid
    padded_plaintext = plaintext.ljust(padded_length)
    
    # Create the grid
    grid = ['' for _ in range(num_cols)]
    for i in range(len(padded_plaintext)):
        grid[i % num_cols] += padded_plaintext[i]
    
    # Create the ciphertext by rearranging columns based on the key
    ciphertext = ''.join(grid[int(k) - 1] for k in sorted(range(1, num_cols + 1), key=lambda x: key[x - 1]))
    
    return ciphertext

def decrypt_transposition(ciphertext, key):
    # Create a list to hold the columns
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    # Create a grid with empty strings
    grid = ['' for _ in range(num_cols)]
    
    # Fill the grid with characters from the ciphertext based on the key order
    sorted_key_indices = sorted(range(len(key)), key=lambda x: key[x])
    start_index = 0
    
    for index in sorted_key_indices:
        grid[index] = ciphertext[start_index:start_index + num_rows]
        start_index += num_rows
    
    # Read the grid column by column to reconstruct the plaintext
    plaintext = ''
    for r in range(num_rows):
        for c in range(num_cols):
            plaintext += grid[c][r]
    
    return plaintext.strip()  # Remove any extra spaces

# Example Usage
key = "431256"  # The key determines the column order
plaintext = "hellotherehowareyou"

# Encrypt the plaintext
ciphertext = encrypt_transposition(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = decrypt_transposition(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
