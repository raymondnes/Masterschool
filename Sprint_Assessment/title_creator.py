# Title Creator

# Write a function called title_creator. 
# The function will expect three parameters:
# title (str) - the text for the title.
# char (str) - the character surrounding the text.
# times (int) - the number of times to repeat the character on each side of the title.
# The function will return a formatted title, as shown in the example.

# Example:
# >> print(title_creator(”Welcome to Masterschool”, “=”, 5))
# ”=====Welcome to Masterschool=====”

def title_creator(title, char, times):
  formated_title = char * times + '' + title + '' + char * times
  return formated_title

print(title_creator("Welcome to Masterschool", "=", 5))
