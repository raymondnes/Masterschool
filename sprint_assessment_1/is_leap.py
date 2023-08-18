# Leap year

# A leap year is a special year that contains an additional day. It’s used to keep our calendar in alignment with the Earth's revolutions around the Sun. It takes the Earth about 365.24 days to complete one full orbit around the Sun. As a result, if we didn't add a leap day approximately every 4 years, our calendar would slowly drift out of sync with the Earth's revolutions.
# Determining which years are leap years involves a few rules:
# The year must be evenly divisible by 4.
# Unless it’s also a century year (like 1900, 2000, etc.), and then it must also be divisible by 400 to be considered a leap year.
# Write a function is_leap that takes a year as input (int) and checks whether it's a leap year or not. 
# If it is a leap year, return "Leap year"(str). If it's not a leap year, return "Not a leap year" (str). 

def is_leap(year):
# Check if the year is evenly divisible by 4
    if year % 4 == 0:
# If it is, check if it's a century year
        if year % 100 == 0:
# If it is, check if it's also divisible by 400
            if year % 400 == 0:
# If it is, it's a leap year
                return "Leap year"
            else:
# If it's not, it's not a leap year
                return "Not a leap year"
        else:
 # If it's not a century year, it's a leap year
            return "Leap year"
    else:
 # If it's not evenly divisible by 4, it's not a leap year
        return "Not a leap year"

print(is_leap(2014))
