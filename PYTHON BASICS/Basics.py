print("hello world")
name = "hello Mr. Alex "
print(name)
print(f"name is {name}")

name =  input("what is your name? ")
print(f"hello my name is {name}")


print("\n --- Welcome to The Voting Eligibility Checker ---")
name = input("what is your name? ")
age = int(input ("Please enter your age : "))
if age >= 18 :
    print("you are eligible to vote")
else: 
    print("You are not elgible to vote") 

count = int(input("Enter your starting number :"))
while count < 10 :
    print(f"\n -- {count}---")
    count = count + 1

for num in range (10) :
    print(f"number is now  {num}")

for num in range(1,11) :
    print(f"number is now {num}")


for i in range (5):
    print(f" The voters number is #0{i +2567}")

booth_open = True
while booth_open :
    action = input("Enter 'vote' to cast your vote or 'close' to close the booth :")
    if action == "close":
        booth_open = False #This will break the loop and close the booth
        print("The booth is now closed. Thank you for voting!")

# TESTING FOR THE REVISION STRENGTH
sum = 0
for i in range(1, 20):
    if i % 2 == 0:
        sum = sum + i
print(f"The sum of all even numbers within that range is {sum}")
