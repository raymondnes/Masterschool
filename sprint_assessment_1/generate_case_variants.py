# Generate Case Variants

# A digital advertising platform needs to create variations of headlines in both uppercase and lowercase.
# Write a function called generate_case_variants, that will expect one parameter: text, a string that needs to be converted.
# The function will return a list containing the lowercase and then the uppercase version of the text.

def generate_case_variants(text):
    # Generate the upper case of the text
    upper_case = text.upper()
    # Generate the lower case of the text
    lower_case = text.lower()
    # return a list with lower case and upper case
    return [lower_case, upper_case]

print(generate_case_variants("ray"))
