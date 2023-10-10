import os
import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_sha512(file_path):
    sha512_hash = hashlib.sha512()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(65536), b''):
            sha512_hash.update(chunk)
    return sha512_hash.hexdigest()

def check_integrity():
    file1_path = filedialog.askopenfilename(title="Select the first file")
    file2_path = filedialog.askopenfilename(title="Select the second file")

    if file1_path and file2_path:
        sha512_hash1 = calculate_sha512(file1_path)
        sha512_hash2 = calculate_sha512(file2_path)

        if sha512_hash1 == sha512_hash2:
            result_label.config(text="Files match", fg="green")
        else:
            result_label.config(text="Files differ", fg="red")

# Create the main window
root = tk.Tk()
root.title("File Integrity Checker")

# Create labels and align them
title_label = tk.Label(root, text="File Integrity Checker", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

instructions_label = tk.Label(root, text="Select two files to check their integrity:", font=("Helvetica", 12))
instructions_label.pack()

# Create buttons and align them
check_button = tk.Button(root, text="Check Integrity", command=check_integrity, padx=20, pady=10, font=("Helvetica", 12))
check_button.pack(pady=20)

# Create a label to display the integrity check result
result_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"))
result_label.pack()

# Start the GUI event loop
root.geometry("400x300")
root.mainloop()
