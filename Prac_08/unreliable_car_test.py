"""
CP1404/CP5632 Practical 8
Unreliable car test
"""
from Prac_08.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use unreliable car class."""

    prius = UnreliableCar("Prius", 100, 50)
    prius.drive(40)
    print(prius)


main()