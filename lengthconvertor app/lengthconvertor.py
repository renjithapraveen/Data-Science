import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        print("inches",inches," is centimeters",cm)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Input field
tk.Label(root, text="Enter length in inches:").grid(row=0, column=0, padx=10, pady=10)
entry_inch = tk.Entry(root)
entry_inch.grid(row=0, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
