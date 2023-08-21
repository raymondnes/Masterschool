# Only “A” Words

# words is a list of words that you have to filter.
# Iterate through it, and print only the words that begin with 
# the letter "A" in a new line.

words = ['Apple', 'Banana', 'Avocado', 'Apricot', 'Artichoke', 'Almond', 'Broccoli', 'Asparagus', 'Aloe', 'Anise']
for word in words:
    if word[0] == "A":
        print(word)
    else:
        pass

print("done")
