import random

def intro():
    print("Welcome to the Upside Down! You are a member of the party, and you have been tasked with finding the missing Will Byers.")
    print("As you search for Will, you will encounter strange and dangerous creatures. Use your wits and your weapons to survive and complete your mission.")

def choice():
    print("\nWhat would you like to do?")
    print("1. Continue searching for Will")
    print("2. Check your inventory")
    print("3. Use a weapon")
    print("4. Run away")
    choice = input("Enter the number of your choice: ")
    return int(choice)

def search():
    chance = random.randint(1, 5)
    if chance == 1:
        print("\nYou have stumbled upon a pack of Demogorgons!")
        fight()
    elif chance == 2:
        print("\nYou have stumbled upon a group of Mind Flayers!")
        fight()
    elif chance == 3:
        find_will()
    elif chance == 4:
        find_weapon()
    else:
        print("\nYou continue searching, but you don't find anything.")

def find_will():
    print("\nYou have found Will Byers!")
    print("Congratulations, you have completed your mission and saved Will! Game over.")
    exit()

def find_weapon():
    inventory = []
    weapon_list = ["baseball bat", "hammer", "wrench", "scissors"]
    weapon = random.choice(weapon_list)
    print(f"\nYou have found a {weapon}! It has been added to your inventory.")
    inventory += [weapon]

def fight():
    print("\nWhat would you like to do?")
    print("1. Fight")
    print("2. Use a weapon")
    print("3. Run away")
    choice = input("Enter the number of your choice: ")
    if int(choice) == 1:
        outcome = random.randint(1, 2)
        if outcome == 1:
            print("\nYou manage to defeat the creatures and continue your search for Will.")
        else:
            print("\nYou are no match for the creatures and are killed. Game over.")
            exit()
    elif int(choice) == 2:
        use_weapon()
    else:
        run_away()

def use_weapon():
    if inventory:
        weapon_list = ["baseball bat", "hammer", "wrench", "scissors"]
        weapon = weapon_list
        print("\nWhat weapon would you like to use?")
        weapons = f"{weapon}, "
        print(f"\nYou have the following weapons in your inventory: {weapons}")
        choice = input("Enter the name of the weapon you want to u1se: ")
        weapon = choice
        messages = {
            "baseball bat": "\nYou swing the baseball bat and manage to fend off the creatures. You continue your search for Will.",
            "hammer": "\nYou swing the hammer and manage to fend off the creatures. You continue your search for Will.",
            "wrench": "\nYou swing the wrench and manage to fend off the creatures. You continue your search for Will.",
            "scissors": "\nYou swing the scissors and manage to fend off the creatures. You continue your search for Will."
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