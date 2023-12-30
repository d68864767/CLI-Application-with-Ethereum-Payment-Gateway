```python
# security.py

from cryptography.fernet import Fernet
from config import ETH_WALLET_API_KEY

# Generate a key for encryption and decryption
# You should ideally save this key somewhere safe and not expose it in your code
# For the purpose of this example, we'll generate a new key each time
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    """
    Encrypts the provided data using Fernet symmetric encryption.

    Parameters:
    data (str): The data to encrypt.

    Returns:
    bytes: The encrypted data.
    """
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt_data(cipher_text):
    """
    Decrypts the provided cipher text using Fernet symmetric encryption.

    Parameters:
    cipher_text (bytes): The cipher text to decrypt.

    Returns:
    str: The decrypted data.
    """
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

# Encrypt the Ethereum Wallet API Key
encrypted_api_key = encrypt_data(ETH_WALLET_API_KEY)

# Decrypt the Ethereum Wallet API Key
# You would do this when you need to use the API Key
decrypted_api_key = decrypt_data(encrypted_api_key)
```
