# Average Grade

# Write a function called average_grade, that accepts three arguments, representing three exam grades (ints).
# The function should return the average grade, as int (it’s ok to floor the average grade).
# No need to call the function (You can do it for testing purposes).
# Remember to use meaningful names for the parameters.

def average_grade(exam1, exam2, exam3):
    return (exam1 + exam2 + exam3) // 3

print(average_grade(10, 20, 20))
