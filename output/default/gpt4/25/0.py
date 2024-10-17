import random
import string

def generate_random_password(length=12):
    """Generate a random password with the specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    if length > 4:
        all_characters = lower + upper + digits + symbols
        password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
print(generate_random_password(12))