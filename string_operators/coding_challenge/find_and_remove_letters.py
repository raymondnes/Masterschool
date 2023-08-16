# Find and Remove Letters

# Define a function named remove_first_letter_occurrences that will accept a single string as its argument.
# The function should identify the first character in the string, and then remove all of its occurrences from the string, and return the new string.

def remove_first_letter_occurrences(word):
    if len(word) == 0:
        return word
    else:
        first_char = word[0]
        return word.replace(first_char, "")
# Main code
result = remove_first_letter_occurrences("titanic") 
print(result)  # Should print: ianic

# This function takes a string word as an argument and first checks if the string is empty. If it is, the function returns the empty string. Otherwise, it extracts the first character of the string using indexing and assigns it to the variable first_char. It then uses the replace method to replace all occurrences of first_char in the string with an empty string, effectively removing them from the string.
