# Currency Convertor

# Write a function called usd_to_yuan, that will get one parameter - An amount of money in US Dollars (int)
# The function will convert the amount to the equivalent amount in Chinese Yuan, and return the result (float).
# Assume that the current exchange rate is 7.15 Yuans for every US Dollar.

# Example:
# >> print(usd_to_yuan(10))
# 71.5


def usd_to_yuan(dollar):
  yuan_value = dollar * 7.15
  return yuan_value

print(usd_to_yuan(10))
