# This is a dinner guest list

# Function to get a valid 'y' or 'n' response
def get_yes_or_no(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ["y","n"]:
                return response
            else:
                print("Invalid input Please enter 'y' or 'n'. ")

# Function to get a valid number input(only integers)
def get_valid_number(prompt):
    while True:
        response = input(prompt).strip()
        if response.isdigit() and int(response) > 0: # Checks if the response is a positive integer
            return int(response)
        else:
            print("Invalid input. Please enter a valid positive number.")

# Function to get a valid name input (only letters)
def get_valid_name(prompt):
    while True:
        response = input(prompt).strip()
        if response.isalpha(): # Checks if the response contains only alphabetic characters
            return response.title() # Capitalizes the first letter of each word
        else:
            print("Invalid input. Please enter only letters.")

# Main game loop
while True:
    # Function that greets the user and ask for their name
    user_name = get_valid_name("What is your name? ") # get_valid_name ensures only letters
    print(f"Welcome {user_name}, this is a dinner inviting list program!")
    print("Lets start this Taco Party!!!")

    # Create an empty guest list
    guest = []

    # Ask the user how many people they would like to add to the list
    num_people = get_valid_number(f"{user_name}, how many people would you like to invite? ") # get_valid_number ensure a valid integer
    
    # Loop that runs until the num_people that you invited in the list are over
    for _ in range(num_people):
        guest_name = get_valid_name("Whats the name of the guest you want to invite? ") # get_valid_name ensures only letters
        guest.append(guest_name)
        print(f"{guest_name} has been added!")

    # Print invitation messages
    print(f"\nHere are your invitation messages from {user_name}: ")
    for guest_name in guest:
        print(f"🎉 {guest_name}, you are invited to {user_name}'s Taco Party! 🎉")

    # Modify the guest list
    while True:
        print("\nWould you like to modify the guest list?")
        modify_choice = input("Enter [remove], [replace], [add], or [done]: ")

        # Remove a guest from the list
        if modify_choice == "remove":
            eliminate = input("Please enter the name of the guest you want to kick out of the Taco Party: ")
            if eliminate in guest:
                guest.remove(eliminate)
                print(f"{eliminate} has been removed from the list for the Taco Party!")
            else:
                print(f"{eliminate} is not in the list.")

        # Replace a guest
        elif modify_choice == "replace":
            old_name = input("Enter the name of the guest you want to replace: ").strip().title()
            if old_name in guest:
                new_name = input("Enter the new guest's name: ").strip().title()
                guest[guest.index(old_name)] = new_name
                print(f"{old_name} has been replaced with {new_name}!")
            else:
                print(f"{old_name} is not in the list.")

        # Add a new guest
        elif modify_choice == "add":
            new_guest = input("Enter the new guest's name: ").strip().title()
            guest.append(new_guest)
            print(f"{new_guest} has been added!")    

        # Exit modification
        elif modify_choice == "done":
            break
        else:
            print("Invalid choice. Please enter [remove], [replace], [add], or [done].")

    # Ask if the user wants to play again
    play_again = get_yes_or_no("\nDo you want to play again? (y/n):")
    if play_again ==  "n":
        print(f"Thanks for playing, {user_name}! See you next time!")
        break # Exit the game loop