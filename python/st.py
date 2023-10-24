import random

counter = 0
inventory_list = []


def intro():
    print(
        "Welcome to the Upside Down! You are a member of the party, and you have been tasked with finding the missing Will Byers."
    )
    print(
        "As you search for Will, you will encounter strange and dangerous creatures. Use your wits and your weapons to survive and complete your mission."
    )


def choice():
    global counter
    counter += 1
    if counter > 2:
        print("\nWhat would you like to do next? 1 - search, 2 - inventory")
    else:
        print("\nWhat would you like to do?")
        print("1. Continue searching for Will")
        print("2. Check your inventory")
    choice = input("Enter the number of your choice: ")
    return int(choice)

def search():
    chance = random.randint(1, 100)
    if chance <= 20:
        enemy = random.choice(["Demogorgons", "Mind Flayers"])
        print(f"\nYou have stumbled upon a group of {enemy}!")
        fight()
    elif chance <= 30:
        find_will()
    elif chance <= 40:
        find_weapon()
    else:
        print("\nYou continue searching, but you don't find anything.")

def find_will():
    print("\nYou have found Will Byers!")
    print("Congratulations, you have completed your mission and saved Will! Game over.")
    exit()


def find_weapon():
    weapon_list = ["scissors", "wrench", "hammer", "baseball bat"]
    weapon_probabilities = [0.25, 0.25, 0.25, 0.25]
    weapon = random.choices(weapon_list, weights=weapon_probabilities, k=1)[0]
    print(f"\nYou have found a {weapon}! It has been added to your inventory.")
    inventory_list.append(weapon)


def fight():
    print("\nWhat would you like to do?")
    print("1. Fight")
    print("2. Use a weapon")
    print("3. Run away")
    choice = input("Enter the number of your choice: ")
    if int(choice) == 1:
        outcome = random.randint(1, 2)
        if outcome == 1:
            print(
                "\nYou manage to defeat the creatures and continue your search for Will."
            )
        else:
            print("\nYou are no match for the creatures and are killed. Game over.")
            exit()
    elif int(choice) == 2:
        use_weapon()
    else:
        run_away()


def use_weapon():
    if inventory_list:
        weapon = inventory_list[-1]  # Fetch the last item in the list
        messages = {
            "baseball bat": "\nYou swing the baseball bat and manage to fend off the creatures. You continue your search for Will.",
            "hammer": "\nYou swing the hammer and manage to fend off the creatures. You continue your search for Will.",
            "wrench": "\nYou swing the wrench and manage to fend off the creatures. You continue your search for Will.",
            "scissors": "\nYou swing the scissors and manage to fend off the creatures. You continue your search for Will.",
        }
        print(messages[weapon])
    else:
        print("\nYou don't have any weapons.")


def run_away():
    outcome = random.randint(1, 3)
    if inventory != None:
        outcome += 1
    if outcome == 1 or outcome == 2:
        print("\nYou are unable to outrun the creatures and are killed. Game over.")
        exit()
    else:
        print("\nYou manage to run away and continue your search for Will.")


def inventory():
    if inventory_list:
        print("\nYou have the following items in your inventory:")
        for item in inventory_list:
            print(f"- {item}")
    else:
        print("\nYou don't have any items in your inventory.")


def main():
    intro()
    while True:
        user_choice = choice()
        if user_choice == 1:
            search()
        elif user_choice == 2:
            inventory()
        elif user_choice == 3:
            use_weapon()
        else:
            run_away()


main()

# Oh dear, a Stranger Things-inspired game.
# This is a text-based game that is incomplete.
# You can search for Will, find weapons, and fight
# monsters. Spooky, right?
#
# I'm still working on this, so it's not finished yet.
# I'm surprised it works as well as it does. Or tries to.
