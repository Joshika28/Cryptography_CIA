import string

ALPHABET = string.ascii_uppercase

def running_key_encrypt(plaintext, running_key):
    plaintext = plaintext.replace(" ", "").upper()
    running_key = running_key.replace(" ", "").upper()

    ciphertext = ""
    for p, k in zip(plaintext, running_key):
        if p in ALPHABET and k in ALPHABET:
            shift = ALPHABET.index(k)
            c = ALPHABET[(ALPHABET.index(p) + shift) % 26]
            ciphertext += c
    return ciphertext


def running_key_decrypt(ciphertext, running_key):
    ciphertext = ciphertext.replace(" ", "").upper()
    running_key = running_key.replace(" ", "").upper()

    plaintext = ""
    for c, k in zip(ciphertext, running_key):
        if c in ALPHABET and k in ALPHABET:
            shift = ALPHABET.index(k)
            p = ALPHABET[(ALPHABET.index(c) - shift) % 26]
            plaintext += p
    return plaintext


def menu():
    while True:
        print("\n====== RUNNING KEY CIPHER ======")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plaintext = input("\nEnter plaintext: ")
            running_key = input("Enter running key: ")

            if len(running_key) < len(plaintext.replace(" ", "")):
                print("\n[!] ERROR: Running key must be at least as long as plaintext!\n")
                continue

            cipher = running_key_encrypt(plaintext, running_key)
            print("\nCiphertext:", cipher)

        elif choice == "2":
            ciphertext = input("\nEnter ciphertext: ")
            running_key = input("Enter running key: ")

            if len(running_key) < len(ciphertext.replace(" ", "")):
                print("\n[!] ERROR: Running key must be at least as long as ciphertext!\n")
                continue

            plain = running_key_decrypt(ciphertext, running_key)
            print("\nDecrypted plaintext:", plain)

        elif choice == "3":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Run the menu
menu()