#WORKING WITH FUNCTIONS 
#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.



# def greet_username():
#     name = input("Enter your name: ")
#     function_called = f"Hello, {name}! Welcome to Python programming."
#     return function_called


# print(greet_username())

# FUNCTION WITH PARAMETERS
def check_age(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
    
age = int(input("Enter your age: "))
print(check_age(age))


def display_welcome():
    print("Welcome to the Python programming course!")