# Multiplication Table

# Write a function called multi_table that prints a 
# multiplication table of a given number.
# The function will accept one int parameter num and will then 
# print the first 6 multiplications of that number.

num = int(input("Enter a number: "))

def multi_table(num):
  lst = [1, 2, 3, 4, 5, 6]
  for i in lst:
    print(i * num)

multi_table(num)
