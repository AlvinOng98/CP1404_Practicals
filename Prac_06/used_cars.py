"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""

    # 1. limo = Car(100)
    limo = Car("Limo", 100)  # 7. updated with name
    # 2.
    limo.add_fuel(20)
    # 3.
    print("Limo fuel =", limo.fuel)
    # 4.
    limo.drive(115)
    # 5.
    print("Limo odo =", limo.odometer)
    # 6.
    print(limo)


main()