def check_exam_eligibility():
    try:
        name = input("Enter your name: ")
        attendance = float(input("Enter your attendance percentage: "))
        marks = float(input("Enter your average marks: "))

        if attendance >= 75 and marks >= 40:
            print(f"{name}, you are eligible to take the exam.")
        elif attendance < 75 and marks < 40:
            print(f"{name}, you are not eligible due to low attendance and marks.")
        elif attendance < 75:
            print(f"{name}, you are not eligible due to low attendance.")
        else:
            print(f"{name}, you are not eligible due to low marks.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for attendance and marks.")

# Run the function
check_exam_eligibility()
