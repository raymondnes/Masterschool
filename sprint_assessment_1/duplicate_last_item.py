# Duplicate the Last Item

# Write a function called duplicate_last_item. The function will expect one parameter: a list with unknown elements.
# The function will add a copy of the last item to the end of the list, and return the updated list.

def duplicate_last_item(lst):
    # Get the last item in the list
    last_item = lst[-1]
    # Add a copy of the last item to the end of the list
    lst.append(last_item)
    # Return the updated list
    return lst

lst = ["Ray", 3, 5.5]
print(duplicate_last_item(lst))
