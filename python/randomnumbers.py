import random

def generate_random_numbers(n, minimum, maximum):
  # Create an empty list to store the random numbers
  random_numbers = []
  
  # Generate the random numbers
  for i in range(n):
    random_number = random.randint(minimum, maximum)
    random_numbers.append(random_number)
    
  return random_numbers

# Main program
print("Welcome to the random number generator!")

while True:
  # Get the input from the user
  num_numbers = int(input("Enter the number of random numbers to generate: "))
  minimum = int(input("Enter the minimum value for the random numbers: "))
  maximum = int(input("Enter the maximum value for the random numbers: "))

  # Generate and print the random numbers
  random_numbers = generate_random_numbers(num_numbers, minimum, maximum)
  print(f"Random numbers: {random_numbers}")
  
  # Check if the user wants to generate more numbers
  another_set = input("Would you like to generate another set of random numbers? Enter 'Y' for yes or 'N' for no: ")
  if another_set.upper() != 'Y':
    break

print("Thank you for using the random number generator!")

# We start by importing the random module, which provides
# functions for generating random numbers. Next, we define a
# function called generate_random_numbers that generates a list
# of random integers within a given range.
#
# We use a loop to generate n random numbers, using the randint
# function from the random module. The randint function returns a
# random integer within the specified range (inclusive). We store
# the random numbers in a list, and then return the list when the
# loop is finished.
# 
# We start a loop that continues until the user decides to exit.
# Within the loop, we prompt the user to enter the number of random
# numbers to generate, the minimum value, and the maximum value. We
# then call the generate_random_numbers function to generate the list
# of random numbers and print the result.
# 
# Finally, we ask the user if they want to generate another set of random
# numbers. If the user enters 'Y', the loop continues and we prompt the user
# for another set of numbers. If the user enters 'N', the loop breaks
# and then we exit.