# Refactor grade

# In a certain university, it was decided that all grades of an exam should be refactored.
# Write a function named refactor_grade that takes one argument: grade (int). 
# This function should subtract 10 from the grade and then add 20% to it and return the refactored grade.
# Call refactor_grade with 75 and save the result to a variable called new_grade.
# Print the new grade.

def refactor_grade(grade):
    return (grade - 10) * 1.2
    

new_grade = refactor_grade(75)
print(new_grade)
