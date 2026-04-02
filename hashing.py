# hashing.py
# Custom Polynomial Rolling Hash – Original Implementation

def custom_hash(text, base=131, mod=10**9 + 9):
    """
    Custom polynomial rolling hash.
    hash = (text[i] * base^i) % mod
    """
    h = 0
    power = 1

    for ch in text:
        h = (h + (ord(ch) * power)) % mod
        power = (power * base) % mod

    return h

