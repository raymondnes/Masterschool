# Please write a program that prompts the user to enter his age using input.
# The program should then display the message “You have been alive for __ hours”.

age = int(input("What is your age: "))
totalDaysInAYear = 365.25
hoursInADay = 24
hoursInAYear = totalDaysInAYear * hoursInADay
print(f"You have been alive for {age * hoursInAYear} hours")
