# String Manipulation

# Write a program that accepts a string and determines if it's # a palindrome by checking if it reads the same forwards and 
# backwards. The program should also display the reversed string.

def palindrome(var):
# convert the variable to lower and save it to a new var called new_var
    new_var = var.lower()
# create a new variable called reverse_var which reverses the new_var with [::-1]
    reverse_var = (new_var)[::-1]
# write a condition that checks if new_var is equal to reverse_var
    if new_var == reverse_var:
# if it does, print vew_var is a palindrome
        print(f"{new_var} is a palindrome")
# if it doesn't, print new_var is not a palindrome 
    else:
        print(f"{new_var} is not a palindrome")
# print the reversed string
    print(f"The reversed string is {reverse_var}")

palindrome("Ralter")
