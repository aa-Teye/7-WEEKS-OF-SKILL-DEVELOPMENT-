# # NUMBER COMPARISON TOOL 
# # STEP1: GET USER INPUTS 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# # STEP2: COMPARE THE NUMBERS
print("\n --- Comparison Results ---")

if num1 > num2:
    print(f"{num1} is greater than {num2}.")

elif num1 < num2:
    print(f"{num1} is less than {num2}.")

elif num1 == num2: 
    print(f"{num1} is equal to {num2}.")


# Projec2: AGE VERIFICATION TOOL 
required_age = 18 
name = input("Enter your name: ")
age = int(input("\n Enter your age: "))

#Comparison 
iseligible = age >= required_age
print("\n --- Age Verification Result ---")
print(f"{name} is eligible to vote: {iseligible} ")