# Question 4➗

# Create a function named multiple_of_4 that receives a single number as input and returns 0 if the number is a multiple of 4, otherwise it should return the number reminder (do not use if statement)

# Create a function named multiple_of_6 that receives a single number as input and returns 0 if the number is a multiple of 6, otherwise it should return the number reminder (do not use if statement)

# Create a function named multiple_of_6_and_4 that receives a single number and uses multiple_of_4 and multiple_of_6 and returns 0 if the number is a multiple of both of them and return the sum of their reminders if it isn’t (remember, you can’t use if statement)

# Your code here
def multiple_of_4(num):
    return num % 4 or 0

def multiple_of_6(num):
    return num % 6 or 0

def multiple_of_6_and_4(num):
    return (not multiple_of_4(num) and not multiple_of_6(num)) * 0 or (multiple_of_4(num) + multiple_of_6(num))
