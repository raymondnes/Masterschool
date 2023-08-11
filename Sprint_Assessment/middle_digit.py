# Middle digit

# Write a function called middle_digit. 
# The function will expect one parameter called num, which is a 3-digit number (int).
# The function will return the middle digit of the number (int).

# Example:
# icon
# >> print(middle_digit(234))
# 3
# >> print(middle_digit(902))
# 0

def middle_digit(num):
    # Your code here
    # num // 10 is aimed at removing the last digit num
    # % 10 fetches the remainder of the previous step (num // 10)
    middle = (num // 10) % 10
    return middle

print(middle_digit(234))
print(middle_digit(902))
