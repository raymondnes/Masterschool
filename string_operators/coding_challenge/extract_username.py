# Email Username

# Write a function called extract_username that extracts the username part from an email - user@gmail.com, and returns it.

def extract_username(email):
    return email.split("@")[0]

print(extract_username("raynesiama@gmail.com"))

# This function takes an email address email as an argument #and uses the split method to split the email address into two #parts, using the "@" character as the separator. The first #part of the split result is the username, so the function returns this part.

# Note that this implementation assumes that the input string # is a valid email address with a single "@" character #separating the username and domain name. If the input string #is not a valid email address, or if it contains multiple "@" #characters, the function may not work correctly.
