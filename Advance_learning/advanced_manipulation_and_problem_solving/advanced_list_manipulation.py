# Advanced List Manipulation

# Write a program that accepts a list of numbers and a 
# specific number of steps. The program should rotate the list 
# to the right by the provided number of steps and then 
# display the result and the initial input.

# Explanation:

# Rotating a list involves shifting its elements to the right or left by a specified number of positions. When an element is 
# shifted beyond the last position, it is then repositioned at the start of the list.

# Example:

# Suppose you have the list [1, 2, 3, 4, 5] and you're asked 
# to rotate it by 2 steps to the right. After the rotation, 
# the list becomes [4, 5, 1, 2, 3].

def rotate_list(lst, steps):
    # Calculate the number of positions to shift
    shift = steps % len(lst)
    
    # Rotate the list to the right
    rotated_list = lst[-shift:] + lst[:-shift]
    
    # Display the result and the initial input
    print(f"Initial input: {lst}")
    print(f"Rotated list ({steps} steps to the right): {rotated_list}")
