# Prime Checker

# Write a program that accepts a number and checks if it's 
# prime or not. Remember, a prime number is a number greater 
# than 1 that is not divisible by any number other than 1 and itself.

num = int(input("Enter a number: "))

def prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
    else:
        return f"{num} is not a prime number"

check_prime = prime_num(num)

print(check_prime)
