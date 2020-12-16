"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Word occurrences
"""


def main():

    input_str = input("Please enter a string: ")


# function counts occurrences in the string and returns it
# in a dictionary
def occurrences(input_str):
    counts = dict()
    words = input_str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


main()