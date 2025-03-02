# This is a dinner guest list

# Function to get a valid 'y' or 'n' response
def get_yes_or_no(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ["y","n"]:
                return response
            else:
                print("Invalid input Please enter 'y' or 'n'. ")

# Main game loop
while True:
    # Function that greets the user and ask for their name
    user_name = input("What is your name? ").title().strip()
    print(f"Welcome {user_name}, this is a dinner inviting list program!")
    print("Lets start this Taco Party!!!")

    # Create an empty guest list
    guest = []

    # Ask the user how many people they would like to add to the list
    while True:
        try:
            num_people = int(input(f"{user_name} how many people would you like to invite (number only)? "))
            if num_people > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Loop that runs until the num_people that you invited in the list are over
    for num in range(num_people):
        guest_name = input("Whats the name of the guest you want to invite? ")
        guest.append(guest_name)
        print(f"{guest_name} has been added!")

    # Print invitation messages
        print(f"Here is an invitation message from {user_name} for {guest_name}: ")
        for guest_name in guest:
            print(f"Welcome {guest_name} you have been invited to {user_name}'s dinner party")

    # Modify the guest list
    while True:
        print("\nWould you like to modify the guest list?")
        modify_choice = input("Enter [remove], [replace], [add], or [done]: ")

        # Remove a guest from the list
        if modify_choice == "remove":
            eliminate = input("Please enter the name of the you want to kick out of the Taco Party: ")
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
                print(f"{old_name} is not in the list.")
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