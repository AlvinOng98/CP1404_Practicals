"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Word occurrences
"""


def main():

    input_str = input("Please enter a string: ")
    print("")
    print("Text: {}".format(input_str))
    word_count = occurrences(input_str)
    # sort dictionary by using sorted() that sorts into a tuple
    # by keys and then using dict() to put it back into a dictionary
    sorted_word_count = dict(sorted(word_count.items()))
    print("")
    for key, value in sorted_word_count.items():
        print("{:<10} : {:<2}".format(key, value))

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