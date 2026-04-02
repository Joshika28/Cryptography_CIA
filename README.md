# Running Key Cipher + Custom Hash Function
This project implements:
1. A **Running Key Cipher (RKC)** for encryption & decryption  
2. A **Custom Polynomial Rolling Hash** (implemented from scratch — not MD5/SHA)

---

## 🔹 Theory: Running Key Cipher
The Running Key Cipher is a classical polyalphabetic cipher similar to the Vigenère cipher.  
Key characteristics:
- Encryption uses: C = (P + K) mod 26  
- Decryption uses: P = (C - K) mod 26  
- Key is typically a long text (a book paragraph or sentence)
- More secure than Vigenère because key length ≈ plaintext length

In this implementation:
- A repeated/trimmed key is used if the key is shorter/longer.
- Only A–Z are used internally (spaces removed).

---

## 🔹 Theory: Custom Hash Function
Cryptographic libraries are not allowed, so this project uses an **original polynomial rolling hash**.

### Formula  
hash = Σ( text[i] × base^i ) mod M

Where:
- `base = 131` → large prime-ish multiplier for better distribution  
- `mod = 1,000,000,009` → large prime to avoid overflow  
- Prevents collisions better than simple additive XOR hashes  
- Fully implemented from scratch (0% library usage)

---

## 🔹 How to Run the Code
### 1. Clone your GitHub repo
git clone <your_repo_link>
cd project

### 2. Run Test Script

You will see:
- plaintext
- key
- ciphertext
- hash output
- decrypted text (same as original)

---

## 🔹 Worked Examples

### ✔ Example 1
Plaintext: `HELLOWORLD`  
Key: `MAGICKEY`  
Ciphertext: (your output)

Hash: (custom hash output)  
Decrypted: `HELLOWORLD`

### ✔ Example 2
Plaintext: `CRYPTOGRAPHY`  
Key: `SUPERLONGSECRETKEY`  
Ciphertext: (your output)  
Hash: (custom hash output)  
Decrypted: `CRYPTOGRAPHY`

---

## 🔹 Files Included
cipher.py - Running Key Cipher implementation
hashing.py - Custom polynomial rolling hash
test.py - Encrypt → Hash → Decrypt test script
README.md - Theory + Instructions + Examples

---
