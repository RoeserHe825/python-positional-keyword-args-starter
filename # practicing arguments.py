# practicing arguments
# Henry Roeser 
# 11/13/24

# POSITIONAL ARGUMENTS
# Greet the User
def greet_user(first_name,age):
    print(f'Hello, {first_name} you are {age} years old.')

# call/invoke the function
greet_user('Henry', 17)

# Area of a Rectangle
def rect_area(length,width):
    print(f'The rectangle is {length} feet long, {width} feet wide and its area is {length * width} square feet.')

rect_area(10,2)

# Sum of Numbers
def sum(num1,num2,num3):
    print(f'The sum of the three numbers is: {num1 + num2 + num3}')

sum(5,10,15)


# KEYWORD ARGUMENTS
# Greet By Title
def greet_user(title,first_name,last_name):
    print(f'Hello, {title} {first_name} {last_name}.')

greet_user(last_name = 'Roeser', first_name = 'Henry', title = 'Mr.')

# Describe Your pet
def describe_pet(pet_type,pet_name):
    print(f'My {pet_type} is named {pet_name}.')

# call/invoke the function
describe_pet(pet_name = 'Tom', pet_type = 'cat')

# Updated Function
def greet_user(first_name,age):
    print(f'Hello, {first_name} you are {age} years old.')

greet_user(age = 17, first_name ='Henry')