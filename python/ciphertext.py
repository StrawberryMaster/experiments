import secrets
import base64
from cryptography.fernet import Fernet

def generate_key():
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode("utf-8")

def encrypt(plaintext, key):
    cipher = Fernet(key)
    ciphertext = cipher.encrypt(plaintext.encode("utf-8"))
    return ciphertext.decode("utf-8")

def decrypt(ciphertext, key):
    cipher = Fernet(key)
    plaintext = cipher.decrypt(ciphertext.encode("utf-8"))
    return plaintext.decode("utf-8")

def main():
    plaintext = "This is a secret message."
    key = generate_key()
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()