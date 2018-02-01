#!/usr/bin/env python

"""
This script will do the following

- Ask the user to enter a starting and ending number
- Check that the starting number is not less than 1
- Check that the ending number is at least 5 times greater than the starting number
- Create a list of integers in the range of the user's starting and ending numbers
- Print out the number and index of each item in the list that is even
- Sum and print all the odd numbers in the list

"""
# function to obtain the range start
# output will be the user-inputted range start


def first_number():
    # set the start number to a global variable for consumption by the end range function.
    global start_num
    start_num = int(input("Please enter a starting number: "))
    # check to ensure user enters a number greater than 1
    if start_num < 1:
        print("The number must be more than 1.  Try again.")
        first_number()
    else:
        return start_num


# function to obtain the range end
# output will be the user-inputted range end
def end_number():
    # set the end number to a global variable to capture the full range.
    global end_num
    end_num = int(input("Please enter an ending number: "))
    # if the user enters a number less than 5x the range at the start of the list throw an error and retry.
    if end_num < (start_num * 5):
        print("The ending number must be at least five times greater than the starting number.  Try again.")
        end_number()
    else:
        return end_num


# call first and end range numbers
first_number()
end_number()

# compute the full range based on the start and ended input values
# add +1 to end range to make sure last number is counted
full_range = list(range(start_num, end_num+1, 1))

# loop through full range and pull out all even numbers and their index.
# Adding +1 so that the index starts at 1, not zero
print("Even numbers in your list: \n")
for even_index, i in enumerate(full_range):
    if i % 2 == 0:
        # adding +1 to even index so that index starts at 1, not 0
        print("{} is at the {} index\n".format(i, str(even_index+1)))

# create empty list that will eventually be all odd numbers
odd_sum = []
# find all odd numbers in range by finding numbers with a remainder of 1.  Add to odd num list
for j in full_range:
    if j % 2 == 1:
        odd_sum.append(j)

# print the sum of all the odd numbers
print("The sum of your number list is: {} \n".format(sum(odd_sum)))

input("Press any key to quit")
