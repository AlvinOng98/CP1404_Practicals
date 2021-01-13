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
    bill_to_date = 0

    while True:
        choice = display_menu()
        if choice not in options:
            print("Invalid menu choice.")
            continue
        elif choice == "C":
            current_taxi = choose_taxi()
            display_bill(bill_to_date)
        elif choice == "D":
            if current_taxi is None:
                print("Please choose a taxi first.")
            else:
                drive_taxi(current_taxi)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, calculate_price(current_taxi)))
            bill_to_date = update_bill(bill_to_date, current_taxi)
            display_bill(bill_to_date)
        elif choice == "Q":
            print("Total trip cost: ${:.2f}".format(bill_to_date))
            display_taxis()
            break


def update_bill(bill_to_date, current_taxi):
    """function updates the total bill"""
    update_price = bill_to_date + calculate_price(current_taxi)
    return update_price


def display_bill(bill_to_date):
    """function displays total bill"""
    print("Bill to date: ${:.2f}".format(bill_to_date))


def display_taxis():
    """function displays all taxis available"""
    count = 0
    print("Taxis are now:")
    for car in taxis:
        print("{} - {}".format(count, car))
        count += 1


def choose_taxi():
    """function that handles the choosing of taxis"""
    count = 0
    for car in taxis:
        print("{} - {}".format(count, car))
        count += 1
    chosen_taxi = int(input("Choose taxi: "))
    current_taxi = taxis[chosen_taxi]
    return current_taxi


def drive_taxi(current_taxi):
    """function drives the taxi a chosen distance"""
    current_taxi.start_fare()
    distance = int(input("Drive how far?"))
    distance_driven = current_taxi.drive(distance)


def calculate_price(current_taxi):
    """function calculates the price of the trip"""
    return current_taxi.get_fare()


main()