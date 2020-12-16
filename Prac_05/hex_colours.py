"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Hex Colours
"""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "beige": "#f5f5dc", "cadetblue": "#5f9ea0", "cyan1": "#00ffff",
               "firebrick": "#b22222", "gray": "#bebebe", "greenyellow": "#008b00", "hotpink": "#ff69b4",
               "indianred": "#cd5c5c", "khaki": "#f0e68c"}


def main():

    display_colours()
    print("")
    choose_colour()


# this function asks user for input then prints the corresponding colour code
# to colour chosen
def choose_colour():
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in HEX_COLOURS:
            print(colour_name, "is", HEX_COLOURS[colour_name])
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


# function will list out all the available colours
def display_colours():
    for key, value in HEX_COLOURS.items():
        print(key)


main()