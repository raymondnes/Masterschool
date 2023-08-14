# Question 8 🍲 (Super Hard!)
# Without using if statement or any built-in python functions besides int function, write a function named round_up which receives a number (float) and round it up only if needed. For clarification, see the following examples
# Hint: Collaborate in your breakout room to think together on how to solve this challenging problem!

# Your code here
# def round_up(num):
#     return -(int(-num))

def round_up(num):
    decimal_part = num - int(num)
    round_up = decimal_part > 0
    return int(num) + round_up

print(round_up(3.1415))
print(round_up(20.0))


# This sets a boolean variable round_up to True if the decimal part is greater than zero, or False otherwise. It then adds the value of round_up (which is either 0 or 1) to the integer part of the input number using the + operator, which has the effect of rounding up if round_up is True.
