# Even Range

# Write a function called even_range, that takes two integers n and m (int).
# The function will print all the even numbers between n and m.

n = int(input("Enter your first number: "))
m = int(input("Enter your second number: "))

def even_range(n, m):
  for i in range(n, m + 1):
    if i % 2 == 0:
      print(i)
    else:
      pass

even_range(n, m)
