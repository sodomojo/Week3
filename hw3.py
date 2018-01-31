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

start_num = 0
end_num = 0

start_num = int(input("Please enter a starting number: "))
while int(start_num) < 0:
    print("The number must be more than 1.  Try again.")


end_num = int(input("Please enter an ending number: "))
while int(end_num) < (start_num * 5):
    print("The ending number must be at least five times greater than the starting number.  Try again.")


full_range = list(range(start_num, end_num))

print("Even numbers in your list:")
for even_index, i in enumerate(full_range):
    if i % 2 == 0:
        print("{} is at the {} index".format(i, str(even_index)))
        break
for odd_index, i in enumerate(full_range):
    if i % 2 == 1:


