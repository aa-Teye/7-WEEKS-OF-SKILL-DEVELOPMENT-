import time


# power_on = True 
# while power_on:
#     status = input("What is the status of the machine?(on /off):   ")
#     if status == "off":
#         power_on = False
#         print("The machine is now ")


#Countdown Timer for New Year Nockout
# GET WHERE THE COUNTDOWN IS STARTING FORM THE USER 
countdown_start = int(input("Enter the starting point for the countdown: "))
while countdown_start> 0:
    print(countdown_start)
    time.sleep(1)
    countdown_start -= 1
print("Happy New Year!")


# ElectraFlow: Voter Verification and Ballot System
# 1. SETTING UP FIXED DATA
voters_list = ["Alice", "Lilly", "Kwabena,", "Kwame", "Kofi", "Ama", "Esi", "Kojo", "Yaa", "Akua"]
voters_processed = 0 
system_active = True

while system_active:
    print("\n ----Welcome to ElectraFlow: Voter Verification and Ballot System----")
    user_name = input("Please enter your name to verify your eligibility to vote: OR (Type 'OFF' to shutdown the system)_: ")
    age = int(input("Please enter your age: "))

    if user_name.upper() == "OFF":
        system_active = False
        print("Shutting down ElectraFlow. Goodbye!")

    elif user_name in voters_list and age >= 18 :
        print(f"Welcome {user_name}! You are eligible to vote. Please proceed to cast your ballot.")
        voters_processed += 1
    elif user_name in voters_list and age < 18:
        print(f"Sorry {user_name}, you are not eligible to vote due to age restrictions.")
    else:
        print(f"Sorry {user_name}, you are not on the voters list. Please check your name and try again.")

print(f"\n --- System Summary ---")
print(f"Total voters processed: {voters_processed}")

        