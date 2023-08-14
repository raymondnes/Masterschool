# Question 3 🧮 

# Create a function named variable_type which receives a single variable as input and uses the type function to return the following string: Variable type is: X where X is the given variable type (<class 'str'>, <class 'int'>, …)

# Create a function named sum_2 which receives two numbers as input and return their sum

def variable_type(var):
    return f"Variable type is: {type(var)}"

print(variable_type(12))

# Question 2
def sum_2(num1, num2):
    return num1 + num2

print(sum_2(3, 4))
