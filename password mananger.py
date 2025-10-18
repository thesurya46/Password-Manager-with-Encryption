import tkinter as tk
from tkinter import messagebox
import sqlite3
from cryptography.fernet import Fernet
import re

# Generate or load encryption key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

fernet = Fernet(load_key())

# Database setup
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS vault (
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# GUI setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

def check_strength(pwd):
    if len(pwd) < 8:
        return "Weak"
    elif re.search(r"[A-Z]", pwd) and re.search(r"[0-9]", pwd) and re.search(r"[!@#$%^&*]", pwd):
        return "Strong"
    else:
        return "Medium"

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    encrypted_pwd = fernet.encrypt(password.encode())
    cursor.execute("INSERT INTO vault (website, username, password) VALUES (?, ?, ?)",
                   (website, username, encrypted_pwd))
    conn.commit()
    messagebox.showinfo("Saved", f"Password saved.\nStrength: {check_strength(password)}")
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def view_passwords():
    cursor.execute("SELECT website, username, password FROM vault")
    records = cursor.fetchall()
    output = ""
    for site, user, pwd in records:
        decrypted_pwd = fernet.decrypt(pwd).decode()
        output += f"{site} | {user} | {decrypted_pwd}\n"
    messagebox.showinfo("Stored Passwords", output if output else "No records found.")

# GUI layout
tk.Label(root, text="Website").pack()
website_entry = tk.Entry(root, width=40)
website_entry.pack()

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root, width=40)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack()

tk.Button(root, text="Save Password", command=save_password).pack(pady=5)
tk.Button(root, text="View Passwords", command=view_passwords).pack(pady=5)

root.mainloop()