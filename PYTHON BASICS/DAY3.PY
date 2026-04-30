# SIMPLE CALCULATOR PROJECT 
#STEP1 GETR USER INPUTS FOR THE TWO NUMBERS 
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

#STEP2 PERFORM THE ARITHEMETIC OPERATIONS
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2


#DISPLAY THE RESULTS  
print("\n ---Calculator Results---")
print(f"Addition: {number1} + {number2} = {addition}")
print(f"Subtraction: {number1} - {number2} = {subtraction}")
print(f"Multiplication: {number1} * {number2} = {multiplication }")
print(f"Division: {number1} / {number2} = {division}")