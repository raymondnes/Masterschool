# Complete the function age. 
# The function expects one parameter (argument) called year (int).
# The function will return the following string (in this example. when year is 1983):
# "You were born in 1983, so you are about 40 years old".
# Hint: Don’t use print inside the function.

def age(year):
  current_year = 2023
  current_age = current_year - year
  return f"You were born in {year}, so you are about {current_age} years old"

print(age(1995))
