# Your code here
def print_header(cafe_name):
    print(f"{cafe_name}")
    print("----------------")

def calculate_espresso_price(quantity):
    return quantity * 1.5

def calculate_cappuccino_price(quantity):
    return quantity * 2.75

def calculate_latte_price(quantity):
    return quantity * 3.25

def print_body(espresso_qty, cappuccino_qty, latte_qty):
    espresso_price = calculate_espresso_price(espresso_qty)
    cappuccino_price = calculate_cappuccino_price(cappuccino_qty)
    latte_price = calculate_latte_price(latte_qty)
    print(f"{espresso_qty}x Espresso ($1.5) --- ${espresso_price}")
    print(f"{cappuccino_qty}x Cappuccino ($2.75) --- ${cappuccino_price}")
    print(f"{latte_qty}x Latte ($3.25) --- ${latte_price}")

def print_footer(espresso_qty, cappuccino_qty, latte_qty):
    total_price = calculate_espresso_price(espresso_qty) + calculate_cappuccino_price(cappuccino_qty) + calculate_latte_price(latte_qty)
    print("---------------")
    print(f"Total --- ${total_price}")

def print_receipt(cafe_name, espresso_qty, cappuccino_qty, latte_qty):
    print_header(cafe_name)
    print_body(espresso_qty, cappuccino_qty, latte_qty)
    print_footer(espresso_qty, cappuccino_qty, latte_qty)

print_receipt("Developers Cafe", 2, 1, 3)


# print_header: This function takes in a string cafe_name and prints it as the header of the receipt, followed by a line of dashes.
# calculate_espresso_price, calculate_cappuccino_price, and calculate_latte_price: These functions each take in a quantity of a particular coffee type and return the total price for that quantity based on the coffee's price per unit.
# print_body: This function takes in quantities for each of the three coffee types and uses the calculate_*_price functions to compute the total price for each type, then prints out a line for each type that includes the quantity, the name of the coffee, the price per unit, and the total price for that type.
# print_footer: This function takes in quantities for each of the three coffee types and uses the calculate_*_price functions to compute the total price for all three types combined, then prints out a line of dashes followed by the total price.
# print_receipt: This function takes in the name of the cafe and quantities for each of the three coffee types, and calls print_header, print_body, and print_footer to print out the entire receipt.
# When you run this code with print_receipt("Developers Cafe", 2, 1, 3), it will print out a receipt for Developers Cafe with 2 Espressos, 1 Cappuccino, and 3 Lattes. The output should look something like this:

# Developers Cafe
# ---------------
# 2x Espresso ($1.5) --- $3.0
# 1x Cappuccino ($2.75) --- $2.75
# 3x Latte ($3.25) --- $9.75
# ---------------
# Total --- $15.5

