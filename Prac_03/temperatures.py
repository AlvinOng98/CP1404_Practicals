"""
CP1404/CP5632 - Practical 3

Temperature
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
            break
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
            break
        else:
            print("Invalid option")


def convert_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


print("Thank you.")

main()
