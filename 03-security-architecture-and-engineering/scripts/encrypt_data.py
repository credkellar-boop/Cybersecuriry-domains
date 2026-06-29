from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_message(message):
    """Encrypts a message using a generated key."""
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    return f.encrypt(message.encode())

# Usage:
# generate_key()
# print(encrypt_message("This is a secret message"))
