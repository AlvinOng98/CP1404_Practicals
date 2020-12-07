"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Quick picks
"""

import random

def main():

    times = num_picks()
    print(picks_generation())


# function to get user input on how many quick picks they want
def num_picks():

    finished = False
    number_of_picks = 0
    while not finished:
        try:
            number_of_picks = int(input("How many quick picks?"))
            if number_of_picks < 0:
                print("Invalid input")
            else:
                finished = True
        except ValueError:
            print("Invalid input")
    return number_of_picks


# function to randomly generate 6 numbers into a list
def picks_generation():

    pick_list = []
    for i in range(0, 6):
        pick_list.append(random.randint(1, 45))
    return pick_list


main()