# Email checker

# Write a function named valid_email that takes a string as an argument. The function should check the following conditions:

# Does the string contain at least one @  symbol.
# Does the string contain at least one period.
# Is the string length bigger than 5 characters.
# If all correct, print “Valid Email”. Otherwise, print “Invalid email”.

def valid_email(email):
    if "@" in email and "." in email and len(email) > 5:
        print("Valid email")
    else:
        print("Invalid email")
