"""
CP1404/CP5632 Practical 8
Silver service Taxi Test
"""

from Prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    print("The fare is ${:.2f}".format(hummer.get_fare()))


main()
