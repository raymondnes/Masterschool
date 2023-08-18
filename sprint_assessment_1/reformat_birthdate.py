# Reformat Birthdate

# After moving from Europe to the US, Jane found herself constantly struggling with date formats. She decided to write a # simple program to automatically reformat her calendar's American-formatted dates into the more familiar European style.
# Write a function called reformat_date. The function will expect one parameter: date, a string in the format MM-DD-YYYY.
# The function will return the same date as a string in the format of DD/MM/YYYY.

def reformat_date(date):
    # split date into month, day and year
    month, day, year = date.split('-')
    # reformat the date into DD/MM/YYYY
    new_date = f"{day}/{month}/{year}"
    # return the reformated date
    return new_date

print(reformat_date("02-22-1995"))
