# ===============================
# Students Marks & Percentage Charts
# ===============================

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# --- Step 1: Define student names and marks ---
students_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

# --- Step 2: Calculate percentage (out of 50 marks) ---
marks_perc = []
for x in students_marks:
    res = (x / 50) * 100
    marks_perc.append(res)

# Print percentage values for verification
print("Marks Percentage List:", marks_perc)

# --- Step 3: Line chart of marks ---
def marks_line_chart():
    plt.plot(students_names, students_marks, marker='o', color='blue', linestyle='--')
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.grid(True)
    plt.show()

# Call line chart function
marks_line_chart()

# --- Step 4: Bar chart of percentage ---
def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='orange')
    plt.title("Students' Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Percentage (%)")
    plt.show()

# Call bar chart function
percentage_bar_chart()
