# Extract Area Code

# Write a function called extract_area_code.
# The function will expect one parameter: phone_number, a string containing a phone number in the format “(XXX) YYY-ZZZZ".
# The function will return a new string containing the extracted area code.

def extract_area_code(phone_number):
    # extract the area code from the phone number
    area_code = phone_number[1:4]
    #return the area code
    return area_code

print(extract_area_code("(120)291-6932"))

# This function extracts the area code from a phone number 
# in the format (XXX) YYY-ZZZZ by slicing the string to 
# get the characters between the first and fourth positions.
# The extracted area code is then returned as a new string.
