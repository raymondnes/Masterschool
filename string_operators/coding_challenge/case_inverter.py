# Case Inverter

# Create a invert_case function that inverts a word's case.
# The function should return the word with inverted case (for example, “HEllo” will become “heLLO”).

def invert_case(text):
    # Your code here
    inverted_text = ""
    for char in text:
        if char.islower():
            inverted_text += char.upper()
        elif char.isupper():
            inverted_text += char.lower()
        else:
            inverted_text += char
    return inverted_text
text_input = input("Enter a word to check: ")
new_text = invert_case(text_input)
print(new_text)

# This function takes a string word as an argument and creates an empty string inverted_word to store the inverted case version of the word. It then iterates over each character in the word using a for loop and checks if the character is lowercase or uppercase using the islower and isupper methods, respectively. If the character is lowercase, it is converted to uppercase using the upper method and added to inverted_word. If the character is uppercase, it is converted to lowercase using the lower method and added to inverted_word. If the character is neither lowercase nor uppercase (e.g., a number or punctuation mark), it is added to inverted_word as is. Finally, the function returns inverted_word.
