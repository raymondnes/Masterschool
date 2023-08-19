# String and List

# Write a program that takes in a string and returns a list 
# containing all the vowels present in that string. Remember, 
# the vowels are a, e, i, o, u

def get_vowels(string):
    # define the vowel letters into a variable called vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # create an empty list called result
    result = []
    # write a loop that checks for characters in a string
    for char in string:
        # if a char is in vowels and not in result
        if char.lower() in vowels and char not in result:
            # append the char to the result
            result.append(char)
    # return result
    return result
