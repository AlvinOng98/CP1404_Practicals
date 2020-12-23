"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from Prac_06.guitar import Guitar


def main():

    print("My guitars!")
    inputGuitar()


# function to get data of guitars
def inputGuitar():
    guitar = []
    guitar_name = input("Name: ")

    while guitar_name != "":
        year = guitarYear()
        cost = guitarCost()
        print("{} ({}) : ${:.2f} added.".format(guitar_name, year, cost))
        guitar_name = input("Name: ")
    print("...snip...")


# function gets year guitar was made
def guitarYear():
    finished = False
    try:
        guitar_year = int(input("Year: "))
        if guitar_year < 0:
            print("Number must be > 0")
        else:
            finished = True
    except ValueError:
        print("Invalid input")
    return guitar_year


# function gets cost of guitar
def guitarCost():
    finished = False
    try:
        guitar_cost = float(input("Cost: "))
        if guitar_cost < 0:
            print("Number must be > 0")
        else:
            finished = True
    except ValueError:
        print("Invalid input")
    return guitar_cost


main()
