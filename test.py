# test.py
from runningkey import encrypt_running_key, decrypt_running_key
from hashing import custom_hash

# ---- Test Case 1 ----
plaintext1 = "HELLOWORLD"
key1 = "MAGICKEY"

cipher1 = encrypt_running_key(plaintext1, key1)
hash1 = custom_hash(cipher1)
decrypt1 = decrypt_running_key(cipher1, key1)

print("=== Test Case 1 ===")
print("Plaintext :", plaintext1)
print("Key       :", key1)
print("Ciphertext:", cipher1)
print("Hash      :", hash1)
print("Decrypted :", decrypt1)
print()

# ---- Test Case 2 ----
plaintext2 = "CRYPTOGRAPHY"
key2 = "SUPERLONGSECRETKEY"

cipher2 = encrypt_running_key(plaintext2, key2)
hash2 = custom_hash(cipher2)
decrypt2 = decrypt_running_key(cipher2, key2)

print("=== Test Case 2 ===")
print("Plaintext :", plaintext2)
print("Key       :", key2)
print("Ciphertext:", cipher2)
print("Hash      :", hash2)
print("Decrypted :", decrypt2)