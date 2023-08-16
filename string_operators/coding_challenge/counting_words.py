# Counting Words
# Write a function count_words that takes a sentence as an argument and returns the number of words in it, based on the count of spaces.
# Assume the sentence doesn't contain any punctuation

def count_words(sentence):
    # your code here
    return len(sentence.split())

num_words = count_words("The Titanic was a luxury British steamship")  
print(f"Number of words is: {num_words}")  # Should print: 7

# This function takes a string sentence as an argument and uses the split method to split the string into a list of words, using whitespace characters (spaces, tabs, and newlines) as the separator. The function then returns the length of this list, which corresponds to the number of words in the sentence.
