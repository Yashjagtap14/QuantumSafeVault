import tkinter as tk
from tkinter import filedialog, messagebox
from crypto.aes_module import encrypt_file, decrypt_file

def select_file():
    return filedialog.askopenfilename()

def encrypt_action():
    file = select_file()
    pwd = password_entry.get()
    if file and pwd:
        out = encrypt_file(file, pwd)
        messagebox.showinfo("Success", f"Encrypted: {out}")

def decrypt_action():
    file = select_file()
    pwd = password_entry.get()
    if file and pwd:
        out = decrypt_file(file, pwd)
        messagebox.showinfo("Success", f"Decrypted: {out}")

root = tk.Tk()
root.title("Quantum-Safe Secure Vault")

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", command=encrypt_action).pack(pady=5)
tk.Button(root, text="Decrypt File", command=decrypt_action).pack(pady=5)

root.mainloop()
