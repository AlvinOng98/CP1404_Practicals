"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from Prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar = Guitar(guitar_name, int(input("Year: ")), float(input("Cost: ")))
        guitars.append(guitar)
        print("{} ({}) : ${} added.".format(guitar.name, guitar.year, guitar.cost))
        guitar_name = input("Name: ")
    print("\n...snip...\n")
    print("These are my guitars: ")
    i = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = ""
        else:
            vintage_string = "(vintage)"
        print("Guitar {}: {:<15} ({}), worth ${:<10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))
        i += 1


main()
