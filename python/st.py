import random
from typing import List, Dict, Optional
from dataclasses import dataclass
import time
import sys


@dataclass
class Weapon:
    name: str
    damage: int
    durability: int
    description: str


@dataclass
class Enemy:
    name: str
    health: int
    damage: int
    description: str


class Player:
    def __init__(self):
        self.health = 100
        self.inventory: List[Weapon] = []
        self.has_flashlight = False
        self.has_walkie_talkie = False
        self.locations_searched = set()
        self.friends_found = set()


class StrangerThingsGame:
    def __init__(self):
        self.player = Player()
        self.initialize_game_data()

    def initialize_game_data(self):
        self.weapons = {
            "baseball bat": Weapon(
                "baseball bat",
                30,
                5,
                "Steve's signature weapon, perfect for swinging at Demogorgons",
            ),
            "slingshot": Weapon(
                "slingshot", 15, 8, "Lucas's weapon of choice, good for distraction"
            ),
            "nail bat": Weapon(
                "nail bat",
                40,
                3,
                "A modified baseball bat with nails - extremely effective but fragile",
            ),
            "hammer": Weapon("hammer", 25, 4, "A sturdy workshop hammer"),
            "scissors": Weapon("scissors", 20, 6, "Sharp but requires close combat"),
        }

        self.enemies = {
            "Demogorgon": Enemy(
                "Demogorgon",
                80,
                35,
                "A terrifying creature from the Upside Down with a flower-like head",
            ),
            "Mind Flayer": Enemy(
                "Mind Flayer",
                100,
                45,
                "A massive shadow monster that controls the hive mind",
            ),
            "Demodogs": Enemy(
                "Demodogs",
                40,
                25,
                "Smaller but equally dangerous dog-like creatures from the Upside Down",
            ),
            "Vecna": Enemy(
                "Vecna",
                120,
                50,
                "A powerful being with psychic abilities and a dark past",
            ),
        }

        self.locations = [
            "Hawkins Lab",
            "The Upside Down",
            "Starcourt Mall",
            "Hawkins Middle School",
            "Bradley's Big Buy",
            "The Wheeler House",
            "Castle Byers",
            "The Quarry",
        ]

        self.friends = ["Eleven", "Mike", "Dustin", "Lucas", "Max", "Steve"]

    def type_text(self, text: str, delay: float = 0.03):
        """Type out text with a delay for dramatic effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def intro(self):
        self.type_text("\n=== WELCOME TO THE UPSIDE DOWN ===", 0.05)
        time.sleep(1)
        self.type_text(
            "\nThe year is 1983. Will Byers has disappeared in Hawkins, Indiana.", 0.03
        )
        time.sleep(0.5)
        self.type_text(
            "Strange things are happening, and you've joined the search party.", 0.03
        )
        time.sleep(0.5)
        self.type_text("But this is no ordinary missing person case...", 0.03)
        time.sleep(1)

    def display_status(self):
        print("\n=== STATUS ===")
        print(f"Health: {'❤️' * (self.player.health // 20)}")
        print(
            f"Locations searched: {len(self.player.locations_searched)}/{len(self.locations)}"
        )
        print(f"Friends found: {len(self.player.friends_found)}/{len(self.friends)}")
        if self.player.has_flashlight:
            print("Equipment: 🔦 Flashlight")
        if self.player.has_walkie_talkie:
            print("Equipment: 📻 Walkie-talkie")

    def search_location(self):
        if len(self.player.locations_searched) == len(self.locations):
            self.type_text(
                "\nYou've searched all known locations! Will must be somewhere else..."
            )
            return

        available_locations = [
            loc for loc in self.locations if loc not in self.player.locations_searched
        ]
        location = random.choice(available_locations)
        self.player.locations_searched.add(location)

        self.type_text(f"\nSearching {location}...")
        time.sleep(1)

        # random events based on location
        chance = random.randint(1, 100)

        if location == "The Upside Down":
            chance -= 20  # if in upside down, more likely to find something

        if chance <= 30:
            self.encounter_enemy()
        elif chance <= 45:
            self.find_friend()
        elif chance <= 60:
            self.find_item()
        elif chance <= 70:
            self.find_special_item()
        else:
            self.type_text("\nYou search carefully but find nothing of interest...")
            if self.player.has_flashlight:
                self.type_text(
                    "Your flashlight reveals some strange markings on the walls..."
                )

    def find_special_item(self):
        if not self.player.has_flashlight and random.random() < 0.5:
            self.type_text(
                "\nYou found a flashlight! This will help you search dark places."
            )
            self.player.has_flashlight = True
        elif not self.player.has_walkie_talkie:
            self.type_text(
                "\nYou found a walkie-talkie! You can now call for help in dangerous situations."
            )
            self.player.has_walkie_talkie = True
        else:
            self.find_item()

    def find_friend(self):
        available_friends = [
            f for f in self.friends if f not in self.player.friends_found
        ]
        if not available_friends:
            self.type_text(
                "\nYou've found all your friends, but Will is still missing..."
            )
            return

        friend = random.choice(available_friends)
        self.player.friends_found.add(friend)

        self.type_text(f"\nYou found {friend}!")
        if friend == "Eleven":
            self.type_text("She can help you with her psychic powers!")
            self.player.health = min(100, self.player.health + 30)
        elif friend == "Steve":
            self.type_text("He gives you his signature nail bat!")
            self.player.inventory.append(self.weapons["nail bat"])
        else:
            self.type_text(f"{friend} joins your search party!")

    def find_item(self):
        available_weapons = [
            w
            for w in self.weapons.values()
            if all(existing.name != w.name for existing in self.player.inventory)
        ]
        if not available_weapons:
            self.type_text("\nYou found some supplies and recover some health!")
            self.player.health = min(100, self.player.health + 20)
            return

        weapon = random.choice(available_weapons)
        self.player.inventory.append(weapon)
        self.type_text(f"\nYou found a {weapon.name}!")
        self.type_text(weapon.description)

    def encounter_enemy(self):
        enemy = random.choice(list(self.enemies.values()))
        self.type_text(f"\n! DANGER ! You've encountered a {enemy.name}!")
        self.type_text(enemy.description)

        while enemy.health > 0 and self.player.health > 0:
            print("\nWhat would you like to do?")
            print("1. Fight")
            print("2. Use weapon")
            if self.player.has_walkie_talkie:
                print("3. Call for help")
            print("4. Try to run")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                damage = random.randint(10, 25)
                enemy.health -= damage
                self.type_text(
                    f"\nYou attack the {enemy.name} and deal {damage} damage!"
                )

                if enemy.health > 0:
                    self.take_damage(enemy.damage)

            elif choice == "2":
                if not self.player.inventory:
                    self.type_text("\nYou don't have any weapons!")
                    continue

                print("\nChoose your weapon:")
                for i, weapon in enumerate(self.player.inventory, 1):
                    print(
                        f"{i}. {weapon.name} (Damage: {weapon.damage}, Uses left: {weapon.durability})"
                    )

                try:
                    weapon_choice = int(input("\nEnter weapon number: ")) - 1
                    weapon = self.player.inventory[weapon_choice]

                    enemy.health -= weapon.damage
                    weapon.durability -= 1
                    self.type_text(
                        f"\nYou attack with {weapon.name} and deal {weapon.damage} damage!"
                    )

                    if weapon.durability <= 0:
                        self.type_text(f"\nYour {weapon.name} breaks!")
                        self.player.inventory.remove(weapon)

                    if enemy.health > 0:
                        self.take_damage(
                            enemy.damage // 2
                        )  # lower damage if player uses weapon

                except (ValueError, IndexError):
                    self.type_text("\nInvalid weapon choice!")

            elif choice == "3" and self.player.has_walkie_talkie:
                if self.player.friends_found:
                    friend = random.choice(list(self.player.friends_found))
                    self.type_text(f"\n{friend} comes to help!")
                    enemy.health -= 50
                    if enemy.health > 0:
                        self.take_damage(enemy.damage // 3)
                else:
                    self.type_text("\nNo one responds to your call...")
                    self.take_damage(enemy.damage)

            elif choice == "4":
                if random.random() < 0.4:
                    self.type_text("\nYou successfully escape!")
                    return
                else:
                    self.type_text("\nYou couldn't escape!")
                    self.take_damage(enemy.damage)

            if enemy.health <= 0:
                self.type_text(f"\nYou defeated the {enemy.name}!")
                if random.random() < 0.3:
                    self.find_item()
            elif self.player.health <= 0:
                self.game_over("You were defeated...")

    def take_damage(self, damage):
        self.player.health -= damage
        self.type_text(f"\nYou take {damage} damage! Health: {self.player.health}")

    def check_inventory(self):
        if not self.player.inventory:
            self.type_text("\nYour inventory is empty...")
            return

        print("\n=== INVENTORY ===")
        for weapon in self.player.inventory:
            print(
                f"- {weapon.name} (Damage: {weapon.damage}, Durability: {weapon.durability})"
            )
            print(f"  {weapon.description}")

    def game_over(self, message):
        self.type_text(f"\n=== GAME OVER ===")
        self.type_text(message)
        self.type_text(
            "\nLocations searched: " + ", ".join(self.player.locations_searched)
        )
        self.type_text("Friends found: " + ", ".join(self.player.friends_found))
        sys.exit()

    def check_win_condition(self):
        if (
            len(self.player.locations_searched) >= len(self.locations) * 0.75
            and len(self.player.friends_found) >= len(self.friends) * 0.75
        ):
            self.type_text(
                "\nWith the help of your friends and the knowledge of Hawkins..."
            )
            self.type_text("You finally track down Will's location!")
            self.type_text(
                "\nCongratulations! You've won the game and saved Will Byers!"
            )
            self.game_over("Mission Accomplished!")

    def play(self):
        self.intro()

        while True:
            self.display_status()
            print("\nWhat would you like to do?")
            print("1. Search a new location")
            print("2. Check inventory")
            print("3. Rest and heal (if you have supplies)")
            print("4. Quit game")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                self.search_location()
                self.check_win_condition()
            elif choice == "2":
                self.check_inventory()
            elif choice == "3":
                if random.random() < 0.3:
                    self.player.health = min(100, self.player.health + 20)
                    self.type_text(
                        "\nYou found a quiet moment to rest and recover some health!"
                    )
                else:
                    self.type_text("\nYou couldn't find a safe place to rest...")
            elif choice == "4":
                self.game_over("You gave up the search...")
            else:
                print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    game = StrangerThingsGame()
    game.play()
