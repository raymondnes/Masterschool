# Tons to kg

# Write a function named ship_weight() that takes one argument, weight_in_tons. 
# This function should convert the weight to kilograms (1 ton is 907.185 kg) and return this value. 
# For this challenge, call ship_weight(52310) (the Titanic's weight in tons).
# Collect and then print the returned value.

def ship_weight(weight_in_tons):
    return weight_in_tons * 907.185
print(ship_weight(52310))
