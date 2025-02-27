# This is a dinner guest list

# Function that greets the user and ask for their name
user_name = input("What is you name? ").title().strip()
print(f"Welcome {user_name}, this is a dinner inviting list program!")

# Create an empty guest list
guest = []

# Ask the user how many people they would like to add to the list
num_people = int(input(f"{user_name} how many people would you like to invite (number only)? "))

# loop that runs until the num_people that you invited in the list are over
for num in range(num_people):

    # Adds the guests name in the guest list
    guest_name = input("Whats the name of the guest you want to invite? ")
    guest.append(guest_name)
    print("Name added!")
    