def is_divisible_by_all_digits(n):
    # Convert number to string to iterate over digits
    for digit in str(n):
        # Convert digit back to integer
        d = int(digit)
        # Check if digit is 0 or not a divisor of the number
        if d == 0 or n % d != 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_divisible_by_all_digits(number):
    print(f"{number} is divisible by all its digits.")
else:
    print(f"{number} is not divisible by all its digits.")
