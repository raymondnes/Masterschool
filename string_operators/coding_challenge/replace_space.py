# A Buggy Program

# The following program was designed to take a user-provided sentence and replace all spaces with underscores. 
# However, due to a few bugs, the modified sentence isn't correctly displayed to the user.
# Try to identify the bugs and make the program work.

def replace_spaces(text):
    return text.replace(" ", "_")
    
sentence = input("Enter a sentence: ")
mod_sentence = replace_spaces(sentence)
print(f"Modified sentence: {mod_sentence}")

# This function takes a string text as an argument and uses the replace method to replace all spaces in the string with underscores. The function then returns the modified string.

# In the main program, the user is prompted to enter a sentence, which is stored in the variable sentence. The replace_spaces function is then called with sentence as its argument, and the modified sentence is returned and stored in the variable modified_sentence. Finally, the modified sentence is printed to the console using an f-string.

# Note that in the original code, the replace method was called on the text string, but the modified string was not returned or stored anywhere. Therefore, the original sentence variable remained unchanged, and the modified sentence was not printed correctly.

