# Caesar Cipher Encryption and Decryption

This is a Python implementation of the Caesar Cipher, a simple encryption technique that shifts each letter in the plaintext by a specified number of places. The program supports both encryption and decryption of messages.

## Features
- **Encryption**: Shifts each letter in the text by a specified shift value to create an encrypted message.
- **Decryption**: Reverses the shift to retrieve the original message.
- Handles both uppercase and lowercase letters.
- Leaves non-alphabetic characters unchanged.

## How It Works
- The program uses the ASCII values of characters to calculate the shifted positions.
- Uppercase and lowercase letters are handled separately to maintain case sensitivity.
- Non-alphabetic characters (e.g., numbers, spaces, punctuation) remain unaltered.

## Prerequisites
- Python 3.x installed on your system.

## Usage

1. **Clone the repository (if applicable)**:
   ```bash
   git clone https://github.com/tholumuzikhuboni/PRODIGY_CY_01.git
   cd caesar-cipher

2. **Run the script**:
   ```bash
   python caesar_cipher.py

3. **Follow the on-screen instructions**:
   - Choose whether to **encrypt** or **decrypt** a message.
   - Enter the message to process.
   - Enter a shift value (integer).
### Example

#### Encryption
**Input**:
- Operation: `encrypt`
- Message: `Hello, World!`
- Shift: `3`

**Output**:
```plaintext
Encrypted message: Khoor, Zruog!

#### Decryption
**Input**:
- Operation: `decrypt`
- Message: `Khoor, Zruog!`
- Shift: `3`

**Output**:
```plaintext
Decrypted message: Hello, World!

## How to Modify
- You can change the shift value to any integer to create more variations of the cipher.
- Adjust the script to read input from a file or save the output to a file for extended functionality.

## Repository Structure
- `caesar_cipher.py`: The Python script implementing the Caesar Cipher.
- `README.md`: Documentation for the project.

## Limitations
- Only supports the English alphabet (A-Z, a-z).
- Shift values outside of 26 are wrapped around (e.g., a shift of 27 is equivalent to a shift of 1).

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Developed by Tholumuzi Khuboni**
