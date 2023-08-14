# Question 7 🎂

# Define a function named birthday_greeting that takes two parameters: name and age.
# Inside the function, use an f-string to return a personalized birthday message that includes the person's name and age. The message should follow this format:
#       Happy {age}th birthday, {name}! Have a fantastic day!

# Call the birthday_greeting function with the same names as questions 

#6. Ask them how old they are so you can display their personalized birthday message.


def birthday_greeting(name, age):
    return f"Happy {age}th birthday, {name}! Have a fantastic day"

print(birthday_greeting("Ray", 26))
