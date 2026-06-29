import hashlib

def hash_file(filename):
    """Generates the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "File not found."

# Usage
# print(hash_file("important_document.pdf"))
