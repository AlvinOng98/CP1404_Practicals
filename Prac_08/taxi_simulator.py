"""
CP1404/CP5632 Practical 8
Taxi Simulator
"""

from Prac_08.taxi import Taxi
from Prac_08.SilverServiceTaxi import SilverServiceTaxi


taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Code for taxi simulator."""

    total_bill = 0
    print("Let's drive!")
    display_menu_options()


def display_menu():
    """function displays options in a menu"""
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>>")
    return choice.upper()


def display_menu_options():
    """function that handles the choosing of options"""

    options = ["Q", "C", "D"]
    current_taxi = None

    while True:
        choice = display_menu()
        if choice not in options:
            print("Invalid menu choice.")
            continue
        elif choice == "C":
            current_taxi = choose_taxi()
        elif choice == "D":
            if current_taxi is None:
                print("Please choose a taxi first.")
            else:
                drive_taxi(current_taxi)
        elif choice == "Q":
            break


def choose_taxi():
    count = 0
    for car in taxis:
        print("{} - {}".format(count, car))
        count += 1
    chosen_taxi = int(input("Choose taxi: "))
    current_taxi = taxis[chosen_taxi]
    return current_taxi


def drive_taxi(current_taxi):
    distance = int(input("Drive how far?"))
    distance_driven = current_taxi.drive(distance)


main()