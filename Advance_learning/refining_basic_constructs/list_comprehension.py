# List Comprehensions

# divisible by seven

# Write a program that generates and displays a list containing all numbers between 1 and 100 that are divisible by 7.

divisible_by_7 = [] # create an empty list
# write a for loop that loops through 1 to 100
for i in range(1, 101): 
    # add a condition that decides if it is divisible by 7
    if i % 7 == 0:
        # append the values of i to the empty list
        divisible_by_7.append(i)

print(divisible_by_7)
