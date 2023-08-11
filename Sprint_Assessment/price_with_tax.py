# Price with Tax

# In a certain country, tax is only applied to the portion of an item's cost that exceeds 100$. The tax rate is 25%.
# Write a function called add_tax. 
# The function will expect one parameter - price (int) - the price of an item in dollars. You can assume the price is larger than 100$.
# The function will return the full price, including taxes (float).

# Example:

# >> print(add_tax(120))
# 125
# >> print(add_tax(425))
# 506.25

def add_tax(price):
  if price > 100:
    tax = (price - 100) * 0.25
  else:
    tax = 0
  total_value = price + tax
  return total_value

print(add_tax(425))
