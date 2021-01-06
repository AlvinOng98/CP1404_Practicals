"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Emails
"""


def main():

    display_emails(users_emails())
    print(users_emails())


# main function that asks for user's email and extracts their name from it
def users_emails():
    emails = dict()
    user_email = input("Email: ")
    user_name = user_email.split('@')[0].replace('.', ' ').title()
    while user_email != "":
        check_username(emails, user_email, user_name)
        user_email = input("Email: ")
        user_name = user_email.split('@')[0].replace('.', ' ').title()
    return emails


# function will check with user if the displayed name is right
def check_username(emails, user_email, user_name):
    name_check = input("Is your name {}? (Y/N) ".format(user_name)).upper()
    if name_check == 'Y' or name_check == '' or name_check == 'YES':
        emails.update({user_name: user_email})
    elif name_check == 'N' or name_check == 'NO':
        user_name = input("Name: ").title()
        emails.update({user_name: user_email})
    else:
        print("Invalid option")
    return emails


# function that prints out the emails with the names
def display_emails(emails):
    for key, value in emails.items():
        print("{} ({})".format(key, value))


main()