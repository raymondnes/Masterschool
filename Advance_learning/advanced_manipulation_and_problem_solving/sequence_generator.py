# Sequence Generator

# Write a program that accepts a number n and generates a list 
# of numbers from 1 to n , but replaces multiples of 3 with 
# the word "Fizz", multiples of 5 with the word "Buzz", and 
# multiples of both 3 and 5 with the word "FizzBuzz".



# collect the user input
n = int(input("Enter a number: "))
# write a function here
def fizzbuzz(n):
    # create an empty list called result
    result = []
    # write a loop that iterates from 1 to the end of n
    for i in range(1, n + 1):
        # write a condition that checks if it is divisible by 3 and 5
        # respectively print FizzBuzz
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # else if it is divisible by 3 alone, print Fizz
        elif i % 3 == 0:
            result.append("Fizz")
        # else if it is divisible by 5 alone, print Buzz
        elif i % 5 == 0:
            result.append("Buzz")
        # otherwise, print i
        else:
            result.append(i)
    return result

result = fizzbuzz(n)

print(result)
