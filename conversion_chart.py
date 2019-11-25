#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program takes the level to grade and returns the middle percentage mark


def mark_finder(level):
    # This'll determine the mark
    marks = {
        "4+": "97.5",
        "4": "90.5",
        "4-": "83",
        "3+": "78",
        "3": "74.5",
        "3-": "71",
        "2+": "68",
        "2": "64.5",
        "2-": "61",
        "1+": "58",
        "1": "54.5",
        "1-": "51",
        "0+": "44.5",
        "0": "34.5",
        "0-": "14.5"
    }

    # process
    if level in marks:
        return(marks[level])
    else:
        return False


def main():
    # Welcome
    print("Ex. level = 4+ >>> Your mark is 97.5%")
    input("Press Enter to start.")

    while True:
        level = input("What is the level: ")
        # runs mark_finder()
        mark = mark_finder(level)
        if mark is False:
            # output
            print("Sorry, you mark could not be determined.")
            print("Try again.")
        else:
            print("Your mark is " + mark + "%")
            break


if __name__ == "__main__":
    main()
