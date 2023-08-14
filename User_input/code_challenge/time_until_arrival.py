# The Titanic's captain wants to know how much time there is left until they arrive at their destination.
# Create a program that asks the user to enter two inputs:
# The distance to the destination in kilometers.
# The average speed in km/h.
# Implement the function time_until_arrival, that takes in these two arguments and gives back the answer.
# The function will calculate and return the time it will take (in hours) to reach the destination by dividing the distance by the speed.
# Then, in the main part of your program, show the message: "It will take you [result] hours to reach your destination.”


def time_until_arrival(distance, speed):
    arrival_time = distance / speed
    return arrival_time

distance = float(input("What is the distance to the destination: "))
speed = float(input("What is the average speed in km/h: "))

# call the function and store the result in the variable
arrival_time = time_until_arrival(distance, speed)

# Main function, where we interact with the user
print(f"It will take you {arrival_time} hours to reach your destination")
