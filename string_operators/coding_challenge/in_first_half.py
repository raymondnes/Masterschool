# Write a function named in_first_half that takes two arguments: a string named word  and a string named char. The function should check if the letter char appears in the first half  of  word. If it is, the function should print "Yes”, otherwise it should print “No”.

def in_first_half(word, char):
  half_length = len(word) // 2 
  if char in word[:half_length]:
    return "Yes"
  else:
    return "No"


# This function first calculates the index of the middle 
# character in the word by dividing the length of the word by 
# 2 using integer division (//). It then checks if the given 
# character is present in the first half of the word using 
# slicing (word[:half_length]). If the character is present in 
# the first half of the word, it prints "Yes". Otherwise, it prints "No".
