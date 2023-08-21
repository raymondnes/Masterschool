# Emphasize the tens

# Write a program that will print all the numbers between 0 and 100.
# For numbers that are divisible by 10 (such as 10, 20, 30...), 
# print an asterisk (*) after the number.
# Hint: Use a condition inside the for loop.

for i in range(0, 101):
  if i % 10 == 0:
    print(f"{i}*")
  else:
    print(i)
