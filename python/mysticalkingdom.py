def play_game():
  # Set up the game world
  entrance = Room("Entrance", "You are at the entrance of the Mystical Kingdom. There is a door to the north and a path to the east.")
  entrance.add_exit("north", "Door", "You open the door and enter the Mystical Kingdom.")
  entrance.add_exit("east", "Path", "You follow the path and come to a fork in the road.")
  
  fork = Room("Fork", "You are at a fork in the road. There is a path to the east and a path to the west.")
  fork.add_exit("east", "Path", "You follow the path and come to a lake.")
  fork.add_exit("west", "Path", "You follow the path and come to a forest.")
  
  lake = Room("Lake", "You are at a lake. There is a path to the west.")
  lake.add_exit("west", "Path", "You follow the path and come back to the fork in the road.")
  
  forest = Room("Forest", "You are in a forest. There is a path to the east.")
  forest.add_exit("east", "Path", "You follow the path and come back to the fork in the road.")
  
  # Start the game
  current_room = entrance
  while True:
    print(current_room.description)
    command = input("What do you want to do? ")
    new_room = current_room.get_exit(command)
    if new_room is not None:
      current_room = new_room
    else:
      print("I'm sorry, I don't understand that command.")
      
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.exits = {}
    
  def add_exit(self, direction, name, description):
    self.exits[direction] = Exit(name, description)
    
  def get_exit(self, direction):
    return self.exits.get(direction)
    
class Exit:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    
play_game()

# In this game, the player is placed in a castle and can explore
# different rooms by entering commands such as "north", "south",
# "east", or "west". The game keeps track of the player's current
# location and allows them to move between rooms by following the
# exits. The game also prints a description of the player's current
# location and any exits that are available.
#
# The game is structured using two classes: Room and Exit. The Room
# class represents a location in the game world, and the Exit class
# represents a way to move between two rooms. Each Room object has a
# dictionary of Exit objects that represent the exits available from
# that room. The player can move between rooms by entering a command
# that matches one of the directions in the dictionary of exits.
# NOTE: WORK IN PROGRESS