# Percent calculation

# Write a function called percent. This function will calculate the percentage of one number relative to another.
# The function will accept two parameters: num1 (int) and num2 (int).
# The function will return the calculated percentage as a string (str).

# Example:
# >> print(percent(155, 500))
# ”31.0%”
# >> print(percent(250, 125))
# ”200.0%”

def percentage(num1, num2):
  percent = (num1 / num2) * 100
  return f"{percent}%"

print(percentage(155, 500))
print(percentage(250, 125))
