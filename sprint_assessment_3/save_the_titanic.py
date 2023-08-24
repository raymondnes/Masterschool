# Initial Titanic position coordinate
# Grid boundaries are 10x10
initial_titanic_pos = [6, 8]

# Initial iceberg position coordinate
# Grid boundaries are 10x10
initial_iceberg_pos = [5, 3]

def auto_pilot_next_step(titanic_pos, ocean_size):
    # List of positions of icebergs in the ocean
    iceberg_positions = [
        [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [9, 3]
    ]
    
    # Get the current row and column of the Titanic
    row, col = titanic_pos
    
    # Check if there is a clear path to the west
    safe_path = True
    for i in range(col - 1, -1, -1):  # Iterate from the current column to the left boundary of the grid
        if [row, i] in iceberg_positions:  # Check if there is an iceberg in this position
            safe_path = False  # If there is an iceberg, it's not safe to go west
            break
    
    if safe_path:
        return 'WEST'  # If it's safe to go west, return 'WEST'
    
    # Find a safe path to the west
    for i in range(row + 1, ocean_size):  # Iterate from the current row to the bottom boundary of the grid
        if [i, col] not in iceberg_positions:  # Check if there is no iceberg in this position
            return 'SOUTH'  # If it's safe to go south, return 'SOUTH'
    
    for i in range(row - 1, -1, -1):  # Iterate from the current row to the top boundary of the grid
        if [i, col] not in iceberg_positions:  # Check if there is no iceberg in this position
            return 'NORTH'  # If it's safe to go north, return 'NORTH'
    
    return 'WEST'  # Default to west if no other direction is chosen

