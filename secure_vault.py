import sys
from crypto import aes_module, hybrid_module, hashing

def menu():
    print("=== Quantum-Safe Secure Vault ===")
    print("1. Encrypt file with password")
    print("2. Decrypt file with password")
    print("3. Generate Kyber keys")
    print("0. Exit")
    return input("Choose option: ")

def main():
    while True:
        choice = menu()
        if choice == "1":
            f = input("File path: ")
            pwd = input("Password: ")
            out = aes_module.encrypt_file(f, pwd)
            print("Encrypted:", out)
        elif choice == "2":
            f = input("Encrypted file path: ")
            pwd = input("Password: ")
            out = aes_module.decrypt_file(f, pwd)
            print("Decrypted:", out)
        elif choice == "3":
            pub, sec = hybrid_module.generate_kyber_keys()
            print("Public key:", pub[:20], "...")
            print("Secret key:", sec[:20], "...")
        elif choice == "0":
            sys.exit(0)

if __name__ == "__main__":
    main()
