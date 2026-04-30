#USING VARIABLES 
name = "Livingston" 
# "name" is an example of a variable, it is a container that holds a value. In this case, the value is "Livingston".
# We can use the variable "name" to store and manipulate data in our program.

print(f"How are you doing {name}?")

#DAY2 PROJECT - PERSONALIZE  GREETING PROGRAM 
#STEP1 ASK THE USER FOR THEIR DETAILS
name = input("What is your name? ")
age = input("What is your age? ")
colour = input("What is your favorite colour? ")

#STEP2 GENERATE A PERSONALIZED MESSAGE
print("\n ----Personalized Greeting Message----")
print(f"hello {name}")
print(f"You are {age} years old")
print(f"Your favorite colour is {colour}")
print("You are now ready to start your python adventure, all the best!")