# Count First Letter

# Write a function called count_first_letter.
# The function will expect one parameter: text, a string containing the text to analyze.
# The function will return the number of times the first letter appears in the text.
# icon

def count_first_letter(text):
    # Get the first letter of the text
    first_letter = text[0]
    # Count the number of times he first letter appears
    count = text.count(first_letter)
    # Return the count
    return count

