# Temperature Conversion

# Write a function named celsius_to_fahrenheit  that will help you convert Celsius temperatures to Fahrenheit.
# This function should accept one argument called celsius and return the equivalent Fahrenheit temperature
# To convert from Celsius to Fahrenheit, multiply the temperature in Celsius by 9/5, then add 32.

def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

result = celsius_to_fahrenheit(50)
print(result)
