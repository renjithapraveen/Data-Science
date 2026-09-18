import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        interest = (principal * rate * time) / 100
        total = principal + interest

        result_label.config(
            text=f"Simple Interest: ₹{interest:.2f}\nTotal Amount: ₹{total:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create Window
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("350x300")

# Heading
title_label = tk.Label(window, text="Simple Interest Calculator",
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Principal
tk.Label(window, text="Principal Amount").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

# Rate
tk.Label(window, text="Interest Rate (%)").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

# Time
tk.Label(window, text="Time (Years)").pack()
time_entry = tk.Entry(window)
time_entry.pack()

# Button
calc_button = tk.Button(window, text="Calculate",
                        command=calculate_interest)
calc_button.pack(pady=10)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()