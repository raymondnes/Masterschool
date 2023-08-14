# To get a number from the user and save it to an int, we can use the same input function, and just convert its return value to int using the type conversion function int

name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"Hi there {name}, you are {age} years old")
print(f"Next year you will be {age + 1} years old")
