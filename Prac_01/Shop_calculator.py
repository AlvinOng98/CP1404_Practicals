"""
CP1404 2020 Practical 1
Student Name: Alvin Ong Zhi Xiang

Program for shop calculators
"""


def main():

    while True:
        items = int(input("Number of items:"))
        if items < 0:
            print("Invalid number of items!")
        else:
            break
    totalPrice = 0
    for i in range(0, items):
        price = float(input("Price of item:"))
        totalPrice += price
    if totalPrice > 100:
        totalPrice = totalPrice*0.9
    print("Total price for {} items is ${:.2f}".format(items, totalPrice))


main()