# list_count

# Create a program that receives two numbers, and counts from
# the first number to the second number

# create an empty list called list_count
list_count = []
# Ask the user to enter the first number
num_start = int(input("Enter the count start point: "))
# Ask the user to enter the last number
num_end = int(input("Enter the count end point: "))

# create a loop that counts from the first number to the last number + 1
for i in range(num_start, num_end + 1):
  # a condition is set to be sure that the counts if divided 
  # by 1 will return 0
    if i % 1 == 0:
      # append the loop to the empty list_count variable
      list_count.append(i)

# print the result
print(list_count)
