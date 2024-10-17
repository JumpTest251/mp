import os
import binascii
import time

def generate_session_token(length=32):
    """
    Generates a secure session token for a web application.

    :param length: Length of the token in bytes (default is 32 bytes)
    :return: A session token represented as a hex string
    """
    # Generate a random token
    token = os.urandom(length)
    # Optionally add a timestamp to the token for extra security
    timestamp = int(time.time()).to_bytes(4, 'big')
    token_with_timestamp = token + timestamp
    # Return the token as a hex string
    return binascii.hexlify(token_with_timestamp).decode('utf-8')

# Example usage:
if __name__ == "__main__":
    print(generate_session_token())