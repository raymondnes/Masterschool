# Birthday Validator

# Let’s write a program that validates if the user entered a valid birthday.
# In the main function, ask the user to input a date in the format DD/MM.
# Write a function called date_checker that will get the input string and validate that both of its parts are valid:
# The day should be a number between 1 and 31.
# The month should be a number between 1 and 12.
# If both conditions are met, print "OK". Otherwise, print “Invalid Birthday!”.

def date_checker(date_str):
    day, month = date_str.split("/")
    if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
        print("OK")
    else:
        print("Invalid Birthday")

def main():
    date_str = input("Enter a date in the format DD/MM: ")
    date_checker(date_str)
