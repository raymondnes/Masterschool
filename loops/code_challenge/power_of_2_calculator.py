def print_square_numbers(): 
    # write a loop that iterates 5 times
    for i in range(5):
        # collect an int input from a user
        num = int(input("Enter a number: "))
        # define the variable square 
        square = num ** 2
        # print the result with a format that takes num and            # square
        print("The square of", num, "is", square)



print_square_numbers()
