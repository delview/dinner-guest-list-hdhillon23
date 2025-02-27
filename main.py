# This is a dinner guest list

# Function that greets the user and ask for their name
user_name = input("What is you name? ").title().strip()
print(f"Welcome {user_name}, this is a dinner inviting list program!")
print("Lets start this Taco Party!!!")

# Create an empty guest list
guest = []

# Ask the user how many people they would like to add to the list
num_people = int(input(f"{user_name} how many people would you like to invite (number only)? "))

# Loop that runs until the num_people that you invited in the list are over
for num in range(num_people):

    # Adds the guests name in the guest list
    guest_name = input("Whats the name of the guest you want to invite? ")
    guest.append(guest_name)
    print("Name added!")

# Loop that prints a message for each guest invited
for num in range(num_people):
    print(f"Here is an invitation message from {user_name} for {guest_name}: ")
    print(f"Welcome {guest_name} you have been invited to {user_name}'s dinner party")

# Remove guest from the list
while True:
    boot = input("Would you like to remove any guest from the list? [y] or [n]")
    if boot == 'y':
        eliminate = input("Please enter the name of the person you want to kick out of the Taco Party: ")
        if eliminate in guest:
            guest.remove(eliminate)
            print(f"{eliminate} has been removed from the list for the Taco Party!")
            print(guest)
        else:
            print("This given guest is already not in the list")
    elif boot == 'n':
