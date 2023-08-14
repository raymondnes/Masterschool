# Remember the formula for converting Celsius to Fahrenheit? It goes like this: (Celsius * 9/5) + 32.
# Now, make a calculator where users can enter any number (including non-whole numbers) in Celsius, and get the result in Fahrenheit.
# Don’t forget to pick meaningful names for your variables and add a comment describing the math behind the conversion.

tempInCelsisus = float(input("Enter temperature in Celsius: "))
# formula for converting celsius to fahrenheit is (Celsius * 9/5) + 32.
fahrenheit = (tempInCelsisus * 9 / 5) + 32
print(f"{fahrenheit} degree in Fahrenheit")
