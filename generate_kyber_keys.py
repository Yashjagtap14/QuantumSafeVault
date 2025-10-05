from kyber_py.kyber import Kyber512

# Generate a public and secret key pair
public_key, secret_key = Kyber512.keygen()

# Print the keys
print("Public Key:", public_key)
print("Secret Key:", secret_key)
