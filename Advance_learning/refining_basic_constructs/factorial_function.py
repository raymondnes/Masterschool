# Factorial function

# Write a program that receives a number as input, the program # should call a function receives a number and returns the 
# factorial of that number. The program should eventually print the factorial result

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))

result = factorial(num)

print(result)
