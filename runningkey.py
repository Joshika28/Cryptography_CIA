# cipher.py
# Running Key Cipher – Encryption & Decryption (ASCII based)

def prepare_key(text, key):
    """Repeat or trim the key to match length of plaintext/ciphertext."""
    key = key.replace(" ", "")
    if len(key) >= len(text):
        return key[:len(text)]
    else:
        # repeat if key is shorter
        repeats = (len(text) // len(key)) + 1
        return (key * repeats)[:len(text)]

def encrypt_running_key(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = prepare_key(plaintext, key).upper()

    ciphertext = ""
    for p, k in zip(plaintext, key):
        c = ((ord(p) - 65) + (ord(k) - 65)) % 26
        ciphertext += chr(c + 65)
    return ciphertext

def decrypt_running_key(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = prepare_key(ciphertext, key).upper()

    plaintext = ""
    for c, k in zip(ciphertext, key):
        p = ((ord(c) - 65) - (ord(k) - 65)) % 26
        plaintext += chr(p + 65)
    return plaintext
