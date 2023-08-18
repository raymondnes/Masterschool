# Currency Converter Pro

# Let’s create a currency converter that can handle two directions of conversion: EUR (€) to USD ($) and vice versa.
# Write a function called convert that will receive a string like "$120" or "€50”, perform the conversion, and return it as a string with the other currency symbol.
# Use the following conversion rates:
# 1 EUR = 1.10 USD
# You may assume that the input to the convert function will be a whole number.
# The returned price string should be up to 2 digits, you can do that using
#       round(float_number, 2)

# Hint: Remember to use type conversion functions to perform arithmetic operations.

def convert(currency):
    # wite a condition that checks the currency value in index 0
    if currency[0] == "$":
    # create a new variable euro_rate that calculates the euro equivalence
    # and adjust the variable type to a float number
        euro_rate = float(currency[1:]) / 1.1
    # return the new value with Euro symbol
        return f"€{euro_rate:.2f}"
    # wite a condition that checks the currency value in index [0]
    elif currency[0] == "€":
    # create a new variable dollar_rate that calculates the euro equivalence
    # and adjust the variable type to a float number
        dollar_rate = float(currency[1:]) * 1.1
    # return the new value with Euro symbol
        return f"${dollar_rate:.2f}"
    # return invalid currency format is none of the currency values are included
    else:
        "Invalid currency format"

print(convert("€50"))
