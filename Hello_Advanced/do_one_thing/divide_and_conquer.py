# Your code here
def divide_and_conquer(num):
    num_of_hundreds = num // 100
    num_of_tens =  (num % 100) // 10
    num_of_ones =  (num % 100) % 10
    print(f"Number: {num}")
    print(f"Ones: {num_of_ones}")
    print(f"Tens: {num_of_tens}")
    print(f"Hundreds: {num_of_hundreds}")
    print(f"{num} = ({num_of_hundreds} * 100) + ({num_of_tens} * 10) + ({num_of_ones} * 1)")


divide_and_conquer(456)
