'''
multiple conditions can be combined using logical operators

    and - returns True if both conditions are True
    or - returns True if one of the conditions is True
    not - returns True if the condition is False
'''

age = 20
name = "John"
is_student = True

print("age > 18 and is_student is", age > 18 and is_student)  # True
print("age > 18 or is_student is", age > 18 or is_student)  # True
print("not is_student is", not is_student)  # False


# Output:
# age > 18 and is_student is True       
# age > 18 or is_student is True
# not is_student is False