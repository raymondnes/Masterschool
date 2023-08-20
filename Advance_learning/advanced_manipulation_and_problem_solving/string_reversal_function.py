# String Reversal Function

# Create a function that accepts a string and returns its 
# reverse. Now, write a program that takes a sentence from the 
# user, splits it into words, and then uses your function to 
# reverse each word in the sentence, but maintains the 
# original order of the words.


# Print the original input and the transformed input at the 
# end of the program run.

def reverse_string(s):
    return s[::-1]

sentence = input("Enter a sentence: ")
words = sentence.split()

# Reverse each word in the sentence
reversed_words = [reverse_string(word) for word in words]

# Join the reversed words to form a new sentence
reversed_sentence = " ".join(reversed_words)

# Print the original input and the transformed input
print("Original input:", sentence)
print("Transformed input:", reversed_sentence)
