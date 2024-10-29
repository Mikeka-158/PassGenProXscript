import string
from password_generator import generate_password

def check_password_strength(password):
    """Check the strength of the password."""
    strength = "Weak"
    if len(password) >= 12 and (any(c.isdigit() for c in password) and
                                 any(c.islower() for c in password) and
                                 any(c.isupper() for c in password) and
                                 any(c in string.punctuation for c in password)):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Moderate"
    return strength

