# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# Given:

# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)

# # You should be able to call the same function using

# show_student(name, age)

# Show Hint
# Assign a different name to function using the assignment (=) operator.

# fun_name = new_name

def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)
