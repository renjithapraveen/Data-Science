# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Input from user
num = int(input("Enter a number: "))
print("The factorial of",num," is ",factorial(num))