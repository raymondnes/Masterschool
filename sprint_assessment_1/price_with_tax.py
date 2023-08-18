# Price with Tax

# In a certain country, only items that cost more than $100 are taxed. The tax rate is 15%.
# Write a function called add_tax. 
# The function will expect one parameter - price (float) - the price of an item in dollars.
# The function will return the full price, including taxes, if applied. (float).

def add_tax(price):
    # write a conditional statement that targets the price value when 
    # in excess of 100
    if price > 100:
    # calculate the tax of the whole price
        tax = price * 0.15
    # return the sum of the price and tax value
        return price + tax
    else:
    # otherwise, return price
        return price

print(add_tax(45))
