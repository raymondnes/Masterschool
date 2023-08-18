# Summer Discount

# A supermarket has started to offer a special summer discount. # To qualify for this discount, a shopping list must contain at least 5 items, and one of them must be “Ice Cream”.
# Write a function called validate_discount that will expect one parameter: a list of strings products.
# If the shopping list qualifies for the discount, return "YES"; otherwise, return "NO".

def validate_discount(products):
    # Check if the shopping list contains at least 5 items and "Ice Cream"
    if "Ice Cream" in products and len(products) >= 5:
    # Return "YES" if the shopping list qualifies for the discount
        return "Yes"
    else:
    # Return "NO" if the shopping list does not qualify for the discount
        return "No"

print(validate_discount(["Shampoo", "Eggs", "Ice Cream", "Soap", "Tissues"]))
