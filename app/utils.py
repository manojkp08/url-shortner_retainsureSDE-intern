# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need

import random
import string

def generate_short_code(length=6):
    """Generate a random 6-char alphanumeric short code."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_url(url):
    """Basic URL validation (minimal check)."""
    return url.startswith(('http://', 'https://'))