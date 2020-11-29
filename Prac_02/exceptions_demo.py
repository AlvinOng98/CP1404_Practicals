"""
CP1404/CP5632 - Practical 2
Student Name: Alvin Ong Zhi Xiang

Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. A ValueError will occur when input is not and integer, for example, "a, b, c" or empty, "".
# 2. A ZeroDivisionError will occur when the input for denominator is 0
# 3. No, not that I know of using try and except handling.
