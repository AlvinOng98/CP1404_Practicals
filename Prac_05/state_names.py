"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
State names in Dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)
print("")

# this loop prints out the elements line by line neatly
for key, value in STATE_NAMES.items():
    print("{:<3} is {:<2}".format(key, value))

# reformat by adding .upper string method so that lowercase inputs also work
print("")
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_NAMES:
        print(state_code, "is", STATE_NAMES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


