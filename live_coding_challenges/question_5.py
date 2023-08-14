# Question 5 🔤

# Create a function named ones_digit that receives a number and return its rightmost digit

# Create a function named tens_digit that receives a number between 100-999 (only) and return its ten digit (the middle digit)

# Create a function named hundreds_digit that receives a number between 100-999 (only) and return its hundreds digit

# Create a function named digit_separator that receives a number between 100-999 (only) and return the following string: number = (hundreds * 100) + (tens * 10) + (ones * 1) 

# where hundreds, tens & ones are replaces with the correct amount. (Hint: use the functions you already wrote to inside digit_separator)


# Your code here
def ones_digit(num):
    return num % 10

def tens_digit(num):
    return (num // 10) % 10

def hundreds_digit(num):
    return num // 100

def digit_seperator(num):
    ones = ones_digit(num)
    tens = tens_digit(num)
    hundreds = hundreds_digit(num)
    result = f"number = ({hundreds} * 100) + ({tens} * 10) + ({ones} * 1)"
    return result

print(digit_seperator(678))
