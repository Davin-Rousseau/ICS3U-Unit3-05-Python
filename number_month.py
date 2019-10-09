#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to input an integer between 1-12
# and tells them the month of the year associated with chosen number


def main():
    # This function prints out a month depending on chosen number

    # input
    chosenNumber = int(input("Enter an integer (1-12): "))
    print("")

    # process
    if chosenNumber == 1:
        # output
        print("January!")
    elif chosenNumber == 2:
        # output
        print("February!")
    elif chosenNumber == 3:
        # output
        print("March!")
    elif chosenNumber == 4:
        # output
        print("April!")
    elif chosenNumber == 5:
        # output
        print("May!")
    elif chosenNumber == 6:
        # output
        print("June!")
    elif chosenNumber == 7:
        # output
        print("July!")
    elif chosenNumber == 8:
        # output
        print("August!")
    elif chosenNumber == 9:
        # output
        print("September!")
    elif chosenNumber == 10:
        # output
        print("October!")
    elif chosenNumber == 11:
        # output
        print("November!")
    elif chosenNumber == 12:
        # output
        print("December!")
    else:
        print("invalid")


if __name__ == "__main__":
    main()
