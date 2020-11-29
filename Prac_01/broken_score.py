"""
CP1404 2020 Practical 1
Student Name: Alvin Ong Zhi Xiang
Fixing broken program to determine score status
"""


def main():

    score = float(input("Enter score:"))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


main()