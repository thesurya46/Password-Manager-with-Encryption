# Password-Manager-with-Encryption
A secure, user-friendly desktop application built with Python that allows users to store and retrieve login credentials with AES-level encryption. Designed with Tkinter for the GUI, SQLite for local data storage, and the cryptography library for password protection, this project demonstrates practical security implementation, clean interface design

## 🚀 Features
- Encrypted Storage: Passwords are encrypted using Fernet (AES-based symmetric encryption) before being saved to the database.
- Password Strength Meter: Provides feedback on password strength (Weak, Medium, Strong) based on length and character diversity.
- Simple GUI: Built with Tkinter, the interface allows users to add, view, and manage credentials easily.
- Local Database: Uses SQLite to store credentials securely on the user's machine.
- Key Management: Automatically generates and stores an encryption key for consistent encryption/decryption across sessions.

## 🧠 Why It Stands Out
- Demonstrates awareness of security best practices in desktop applications.
- Combines GUI design with backend logic, showing full-stack desktop development.
- Uses real-world tools like SQLite and cryptography, making it relevant for job-ready portfolios.
- Easily extensible with features like master password login, search/filter, and export/import.


## ❓ Key Questions & Answers

1. How does your app ensure password security?
It uses Fernet encryption from the cryptography library, which is AES-based and provides symmetric encryption. Passwords are encrypted before being stored in the SQLite database and decrypted only when viewed.

2. Why did you choose SQLite for storage?
SQLite is lightweight, file-based, and perfect for desktop applications. It requires no server setup and integrates easily with Python, making it ideal for local credential storage.

3. How is the encryption key managed?
The app generates a key using Fernet.generate_key() and stores it in a file (secret.key). This key is reused across sessions to ensure consistent encryption/decryption.

4. What does the password strength checker evaluate?
It checks for minimum length, presence of uppercase letters, digits, and special characters. Based on these, it categorizes passwords as Weak, Medium, or Strong.

5. What are potential improvements or next steps?
Adding a master password for authentication, implementing search/filter functionality, exporting/importing encrypted data, and integrating a password generator.

6. How does the GUI enhance usability?
Tkinter provides a simple, responsive interface for entering and viewing credentials. It reduces user friction and makes the app accessible to non-technical users.

## 📦 Setup Instructions
# Install dependencies
pip install cryptography

# Run the application
python password_manager.py


🔒 Future Enhancements
- 🔐 Master password authentication
- 📤 Export/import encrypted vault
- 🔍 Search and filter entries
- 🧮 Password generator with strength presets
- 🌐 Cloud sync or backup option


## 🔍 Deep Dive: What More Can You Show?
1. 🧱 Architecture Overview

## 🧱 Architecture
- **Frontend**: Tkinter GUI for user input and display
- **Backend**: SQLite database for persistent storage
- **Security Layer**: Fernet encryption for password protection
- **Key Management**: Local file-based key storage


You can visualize this with a simple diagram showing how data flows from GUI → encryption → database.

2. 🔐 Security Practices
- Uses symmetric encryption (Fernet) with a securely stored key.
- Passwords are never stored in plaintext.
- Strength checker encourages users to choose safer passwords.
- Future upgrade: Add master password with hashed verification.

3. 📤 Export/Import Feature (Optional Add-on)
You can add buttons to:
- Export all encrypted entries to a .json or .csv file.
- Import them back securely using the same encryption key.
This shows data portability and backup awareness — great for real-world use.

4. 🔍 Search & Filter Functionality
Add a search bar to filter entries by:
- Website name
- Username
- Date added (if you add timestamps)
This improves usability and shows data querying skills.

5. 🧪 Unit Testing (Optional but Impressive)
Use unittest or pytest to test:
- Encryption/decryption logic
- Database insert/retrieve
- Password strength checker
This shows code reliability and professionalism.

## 🙋‍♂️ Author
Created by work.suryasnata@gmail.com
Focused on building secure, accessible, and educational tools using Python and open-source technologies.

