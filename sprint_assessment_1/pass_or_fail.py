# Pass or Fail

# As part of a university course, students were required to take two exams. 
# To successfully complete the course, students needed to fulfill two conditions: 
# Their average grade must be 75 or higher
# They must not receive a failing grade (55 or lower) on either exam.
# Write a function called has_passed. 
# The function will expect two parameters called grade1 and grade2 (ints).
# The function will return a string “PASS” or “FAIL” according to the above conditions.

def has_passed(grade1, grade2):
    if (grade1 + grade2) / 2 >= 75 \
    and grade1 > 55 \
    and grade2 > 55:
        return "PASS"
    else: 
        return "FAIL" 

print(has_passed(90, 80))
