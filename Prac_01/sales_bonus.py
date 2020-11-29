"""
CP1404 2020 Practical 1
Student Name: Alvin Ong Zhi Xiang

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():

    while True:

        sales = float(input("Please enter sales: $"))

        if sales < 0:
            print("You have entered a negative number.")
            break
        elif sales >= 1000:
            bonus = sales*0.15
            print("Your sales bonus is", bonus)
        elif sales < 1000:
            bonus = sales*0.1
            print("Your sales bonus is", bonus)


main()

