
# DUVICrypT0R

![Alt text](https://raw.githubusercontent.com/Menesay/Python-Ransomware/main/duvi_bg.png)

## Overview
DUVICrypT0R is a ransomware script written in Python. It encrypts files in specified directories and then requires a key to decrypt them. The script also changes the desktop background and creates a ransom note instructing the user on how to decrypt their files.

## Features
- **File Encryption:** Encrypts files in user directories and specified drives.
- **File Decryption:** Decrypts the files if the correct key is provided.
- **Key Generation:** Randomly generates a key used for encryption and decryption.
- **Ransom Note:** Creates a ransom note instructing the user to run the decryptor with the correct key.
- **Background Change:** Changes the desktop background to a specified image.

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/DUVICrypT0R.git
   cd DUVICrypT0R
   ```

2. **Install Dependencies:**
   Ensure you have Python and the required libraries installed. You can install the necessary libraries using:
   ```sh
   pip install cryptography
   ```

## Usage
**Running the Script:**
```sh
python DUVICrypT0R.py
```
This will start the encryption process and generate a key saved in `KEY_duvi.txt`.

## Decrypting Files
After running the script, you will be prompted to enter the key for decryption. If the correct key is provided, the script will decrypt the files.

## Important Notes
- **Educational Purposes Only:** This script is for educational purposes and should not be used for malicious activities.
- **Run with Caution:** Running this script will encrypt files on your system, which may cause data loss if not handled properly.

---
