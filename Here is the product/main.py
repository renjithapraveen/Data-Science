import tkinter as tk

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        
        # Clear previous result
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Product: {result}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers!")

# Create main window
window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

# Description label
description = tk.Label(window, text="This application calculates the product of two numbers.")
description.pack(pady=10)

# First number label and entry
label1 = tk.Label(window, text="Enter First Number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

# Second number label and entry
label2 = tk.Label(window, text="Enter Second Number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Calculate button
calc_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Text box to display result
result_text = tk.Text(window, height=2, width=30)
result_text.pack()

# Run the application
window.mainloop()