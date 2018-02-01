# initialize the start and end of the list range
start_num = 0
end_num = 0

def first_number():
    # if the user enters a number less than zero throw an error and retry.
    global start_num
    start_num = int(input("Please enter a starting number: "))
    if start_num < 1:
        print("The number must be more than 1.  Try again.")
        first_number()
    else:
        return start_num


def end_number():
    # if the user enters a number less than 5x the range at the start of the list throw an error and retry.
    global end_num
    end_num = int(input("Please enter an ending number: "))
    if end_num < (start_num * 5):
        print("The ending number must be at least five times greater than the starting number.  Try again.")
        end_number()
    else:
        return end_num

first_number()
end_number()
#compute the full range based on the start and ended input values
full_range = list(range(start_num, end_num))

#loop through full range and pull out all even numbers and their index.  Adding +1 so that the index starts at 1, not zero
print("Even numbers in your list: \n")
for even_index, i in enumerate(full_range):
    if i % 2 == 0:
        print("{} is at the {} index\n".format(i, str(even_index+1)))

#create empty list that will eventually be all odd numbers
odd_sum = []
#find all odd numbers in range by finding numbers with a remainder of 1.  Add to odd num list
for j in full_range:
    if j % 2 == 1:
        odd_sum.append(j)

#print the sum of all the odd numbers
print("The sum of your number list is: {} \n".format(sum(odd_sum)))

input("Press any key to quit")



