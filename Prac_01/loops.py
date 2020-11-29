"""
CP1404 2020 Practical 1
Student Name: Alvin Ong Zhi Xiang

Program for loops
"""


def main():

    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for tens in range(0, 101, 10):
        print(tens, end=' ')
    print()
    for down in range(20, 0, -1):
        print(down, end=' ')
    print()

    n = int(input("Enter number of stars:"))
    for stars in range(0, n):
        print("*", end=' ')
    print()
    for stars in range(0,n):
        for inc in range(0, stars+1):
            print("*", end=' ')
        print()


main()