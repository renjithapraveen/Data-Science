import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        strength = "Please enter a password."
    elif length < 6:
        strength = "Weak"
    elif 6 <= length <= 10:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    result_label.config(text=f"Password Strength: {strength}")

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.resizable(False, False)

# Create and place widgets
label = tk.Label(root, text="Enter your password:", font=('Arial', 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=('Arial', 12))
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))
result_label.pack(pady=5)

# Run the application
root.mainloop()
