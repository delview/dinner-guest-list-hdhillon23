# This is a dinner guest list

# Function that greets the user and ask for their name
user_name = input("What is you name? ").title().strip()
print(f"Welcome {user_name}, this is a dinner inviting list program!")

# Make an empty list
guest = []

# Ask the user how many people they would like to add to the list
num_people = int(input(f"{user_name} how many people would you like to invite (number only)? "))

