# Caesar Cipher Encryption and Decryption by Tholumuzi Khuboni

# Function to encrypt the message
def encrypt(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) +
            shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) +
            shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            result += char
    return result

# Function to decrypt the message
def decrypt(text, shift):
    result = ""
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) -
            shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) -
            shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            result += char
    return result

# Main function to interact with the user
def main():
    # Get user input for the message and shift value
    choice = input("Choose operation: 'encrypt' or 'decrypt': ").strip ().lower()
    text = input("Enter the text ").strip()
    shift = int(input("Enter shift value (integer): ").strip())

    if choice == "encrypt":
        encrypted_message = encrypt(text, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == "decrypt":
        decrypted_message = decrypt(text, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid operation! Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
