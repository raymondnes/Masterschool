# Does it contain vowels?

# Write a function has_vowels which accepts a string as a single argument. The function will check if the string contains at least one of the vowels a, e, i, u or o, If it does, it will print “Yes”. Otherwise, it will print “no”. You may assume the input will be in lowercase entirely. 

def has_vowels(str1):
    if "a" in str1 \
    or "e" in str1 \
    or "i" in str1 \
    or "o" in str1 \
    or "u" in str1:
        return "Yes"
    else:
        return "No"
