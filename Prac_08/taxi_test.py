"""
CP1404/CP5632 Practical 8
Taxi Test
"""
from Prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use taxi class."""

    # Prius 1 (100 fuel, fare = 1.23/km)
    prius = Taxi("Prius 1", 100, 1.23)
    prius.drive(40)
    print(prius, "\nCurrent fare = ${:.2f}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius, "\nCurrent fare = ${:.2f}".format(prius.get_fare()))


main()