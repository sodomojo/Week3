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

range = []

start_num = int(input("Enter a number to start with: "))

while start_num < 0:
    print("The number must be more than 1.  Try again.")
else:
    start_num.append(range)

'''
end_num = int(input("Enter a number to end with: "))

while end_num < (start_num * 5):
    print("The ending number must be at least five times greater than the starting number.  Try again.")
    break


for i in full_list:
    pass
'''



"""
global start_num
global end_num

def range_start():
    start_num = int(input("Enter a number to start with: "))
    while start_num < 0:
        print("The number must be more than 1.  Try again.")
    return start_num

range_start()

def range_end():
    end_num = int(input("Enter a number to end with: "))
    while end_num > (start_num * 5):
        print("The ending number must be at least five times greater than the starting number.  Try again.")
        break
    return end_num


range_end()
"""
#full_range = list(range_start(), range_end())