# Coffee Cost

# You're ordering coffee for your office. A small coffee costs $2, a medium coffee costs $3, and a large coffee costs $4. 
# Write a function coffee_calculator that takes three parameters - the number of each size coffee (ints), and returns the total cost of the order (int).

# Example:
# >> print(coffee_calculator(2, 10, 1))
# 38

def coffee_calculator(small, medium, large):
  small_coffee_prize = 2
  medium_coffee_prize = 3
  large_coffee_prize = 4
  total_order_cost = (small_coffee_prize * small) + (medium_coffee_prize * medium) + (large_coffee_prize * large)
  return total_order_cost

print(coffee_calculator(2, 10, 1))
