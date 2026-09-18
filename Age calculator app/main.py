import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        birth_date = datetime(year, month, day)
        today = datetime.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(
            text=f"Hello {name}! You are {age} years old."
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date values!")

# Create main window
window = tk.Tk()
window.title("Age Calculator App")
window.geometry("400x400")

# Heading
heading = tk.Label(window, text="Age Calculator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Frame for form (side by side layout using grid)
frame = tk.Frame(window)
frame.pack(pady=20)

# Name
tk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Day
tk.Label(frame, text="Day:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_day = tk.Entry(frame)
entry_day.grid(row=1, column=1, padx=10, pady=5)

# Month
tk.Label(frame, text="Month:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_month = tk.Entry(frame)
entry_month.grid(row=2, column=1, padx=10, pady=5)

# Year
tk.Label(frame, text="Year:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_year = tk.Entry(frame)
entry_year.grid(row=3, column=1, padx=10, pady=5)

# Button
calc_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the app
window.mainloop()