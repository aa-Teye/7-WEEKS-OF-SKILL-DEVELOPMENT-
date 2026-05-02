#WORKING WITH FUNCTIONS 
#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.



# def greet_username():
#     name = input("Enter your name: ")
#     function_called = f"Hello, {name}! Welcome to Python programming."
#     return function_called


# print(greet_username())

# FUNCTION WITH PARAMETERS
# We use paraameters when the function needs to with specific data. Parameters are defined in the function definition and can be used within the function to perform operations.
# def check_age(age):
#     if age >= 18:
#         return "You are eligible to vote."
#     else:
#         return "You are not eligible to vote."
    
# age = int(input("Enter your age: "))
# print(check_age(age))

# For this the function doesn't need any parameters to perform its task, so we can define it without parameters. The function simply displays a welcome message when called.  
def display_welcome():
    print("Welcome to the Python programming course!")

display_welcome()


#BASIC MATH QUIZ GAME 
import random 
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator  = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 / num2

