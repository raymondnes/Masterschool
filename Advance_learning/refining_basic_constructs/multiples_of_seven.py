# create a function called multiples of seven, that prints a 
# sub funtion called divisible by 7

def multiples_of_seven():
        divisible_by_7 = [] # create an empty list
        # write a for loop that loops through 1 to 100
        for i in range(1, 101): 
            # add a condition that decides if it is divisible 
            # by 7
            if i % 7 == 0:
                # append the values of i to the empty list
                divisible_by_7.append(i)
        
        print(divisible_by_7)
multiples_of_seven()
