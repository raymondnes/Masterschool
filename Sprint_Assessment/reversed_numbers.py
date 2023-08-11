def reverse_number(number):
    # Your code here
    # convert the number to a string and reverse it
    reverse_str = str(number)[::-1]
    #convert the reversed string back to an integer and return it
    return int(reverse_str)

print(reverse_number(56367))
