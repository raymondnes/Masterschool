# Case Insensitive Comparison

# Comparing two strings in a case-insensitive manner is a very common practice when writing user interfaces. For example, usually, we don't mind if a user enters "Yes" or "yes" or "YES" - we can treat all those situations the same.
# Write a function named are_strings_equal that accepts two strings as its arguments.
# If the strings are equal in a case-insensitive manner, the function should print “Equal”. otherwise, it should print "Not Equal".

def are_strings_equal(str1, str2):
    if str1.lower() == str2.lower(): # convert to lowercase
        print("Equal")
    else:
        print("Not Equal")
# call your function
are_strings_equal("Titanic", "titanic")  # Should print: Equal
are_strings_equal("Titanic", "Bla")  # Should print: Not equal

