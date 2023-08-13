import random

number = random.randint(1, 1000)

num_guesses = 0

guess = int(input("guess a number between 1 and 1000: "))

while guess != number:
  if guess > number:
    print("Too high, try again")
  else:
    print("Too low, try again")
    
  num_guesses += 1
  
  guess = int(input("guess a number between 1 and 1000: "))

print("Congratulations! you have guessed the right number in " + str(num_guesses) + " guesses")
