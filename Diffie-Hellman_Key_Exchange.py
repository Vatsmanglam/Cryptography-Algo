from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes

def diffie_hellman_key_exchange():
    parameters = dh.generate_parameters(generator=2, key_size=512)
    
    private_key_A = parameters.generate_private_key()
    public_key_A = private_key_A.public_key()

    private_key_B = parameters.generate_private_key()
    public_key_B = private_key_B.public_key()

    shared_key_A = private_key_A.exchange(public_key_B)
    shared_key_B = private_key_B.exchange(public_key_A)
    
    assert shared_key_A == shared_key_B
    return shared_key_A

# Example usage
shared_key = diffie_hellman_key_exchange()
print(f"Shared Key: {shared_key}")
