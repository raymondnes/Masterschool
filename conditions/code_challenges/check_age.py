# Implement the function check that accepts a single parameter called age (int).

# The function will print “Adult” if the age is greater or equal to 18.

# The function will print “Baby” if the age is smaller or equal to 3.

def check(age):
    if age >= 18:
        print("Adult")
    elif age <= 3:
        print("Baby")
    else:
        print(f"You are {age} years old")

# Main function
age_input = int(input("Enter your age: "))
check(age_input)
