# Implement a function is_adult that accepts a single parameter called birth_year (int), holding the birth year of a person.
# The function will print “Adult” if the person is older than 18.
# No need to implement user input this time.

def is_adult(birth_year):
    current_year = 2023
    age = current_year - birth_year
    if age > 18:
        print("Adult")
