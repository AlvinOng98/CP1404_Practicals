"""CP1404/CP5632 Practical - Test code to use the Guitar class."""

from Prac_06.guitar import Guitar


def main():

    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

    guitars = [Gibson]

    for guitar in guitars:
        print(guitar)

    print("{} get_age() - Expected 98. Got {}".format(Gibson.name, Guitar.get_age(Gibson)))
    print("{} is_vintage() - Expected True. Got {}".format(Gibson.name, Gibson.is_vintage()))


main()
