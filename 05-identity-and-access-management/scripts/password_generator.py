import secrets
import string

def generate_password(length=16):
    """Generates a cryptographically secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Usage
# print(f"Generated Password: {generate_password()}")
