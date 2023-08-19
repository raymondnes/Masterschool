# Function and Lists

# Design a function that receives a list of numbers as input and returns a new one containing only the even numbers from the original list.


# Call the function from your program with a list of numbers of your choice.

def get_even_numbers(numbers):
    # create an empty list
    even_numbers = []
    # a loop that iterates through the list
    for number in numbers:
        # a condition that checks if it is an even number
        if number % 2 == 0:
            # append even number to the even_numbers list
            even_numbers.append(number)
    # return even_numbers
    return even_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
