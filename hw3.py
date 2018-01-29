#!/usr/bin/env python

"""
Ask the user to enter a starting and ending number
The user must not enter a starting number less than 1
The user must enter an ending number at least 5 times greater than the starting number
Create checks and error messages for the above
Create a list of integers in the range of the user's starting and ending numbers
Print out the number and index of each item in the list that is even
Sum all the odd numbers in the list using a for loop ( hint: append odd numbers to a list and then sum() that list )
Print out the cumulative sum calculated above
 Upload your python file to Canvas.
"""


def user_numbers():
    start_num = input("Enter a number to start with: ")
    start_num = int(start_num)

    if start_num <= 1:
        print("The number must be more than 1.  Try again.")

    end_num = input("Enter a number to end with: ")
    end_num = int(end_num)

    if end_num < start_num * 5:
        print("The ending number must be at least five times greater than the starting number.  Try again.")


user_numbers()

