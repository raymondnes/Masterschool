# Sentence, Period.

# The editor of a local newspaper has a recurring problem - the reporters hand in articles and forget to add a period at the end of the sentences.
# Write a function called period_adder.  The function will expect one parameter called sentence which holds a single sentence (str).
# The function will return the sentence with a single period at the end, regardless of whether there was a period there in the first place.
# The only exception is sentences that end with a “!”, in which case there is no need to add a period.

def add_period(sentence):
# create a variable called period with the period as the value
    period = "."
# write a if statement checking if the period is present in the sentence
    if period in sentence:
# return the sentence untouched
        return sentence
    else:
# otherwise, return the sentence plus period
        return sentence + period


print(add_period("I am a boy"))
