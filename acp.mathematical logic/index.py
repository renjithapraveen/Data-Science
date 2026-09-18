# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all two-digit prime numbers
two_digit_primes = []
for num in range(10, 100):
    if is_prime(num):
        two_digit_primes.append(num)

# Print the result
print("Two-digit prime numbers are:")
print(two_digit_primes)