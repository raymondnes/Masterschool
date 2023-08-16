# Fix the Alien Message

# An alien race sent humans a message, but they have different punctuation marks! We've noticed they consistently use two symbols: "∆" in place of our exclamation mark "!" and "Ω" instead of our question mark "?". 
# Let's help translate this so that everyone on Earth can understand their important message.
# Write a function named translate_punctuation that accepts the alien message as a string.
# Return the translated message, after both replacements.

def translate_punctuation(alien_message):
    trans_message = alien_message.replace("∆", "!")
    final_message = trans_message.replace("Ω", "?")
    return final_message
