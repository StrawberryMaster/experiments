import string
import random

def random_string(length, num_strings):
    choices = string.ascii_letters + string.digits
    return [''.join(random.sample(choices, k=length)) for _ in range(num_strings)]

length = int(input("Enter the length of the random strings: "))
num_strings = int(input("Enter the number of random strings: "))
print(random_string(length, num_strings))

# We are defining a function called "random_string" which takes in two
# parameters, "length" and "num_strings". Within the function, we create
# a variable called "choices" which is a combination of ASCII letters and
# digits. We then use a list comprehension to generate a list of random strings
# by joining a sample of "choices" with a specified length for each iteration in
# the range of "num_strings".
#
# We then ask the user to input the length and number of random strings they want.
# These values are stored as the variables "length" and "num_strings". We then
# print the result of the "random_string" function using these user-specified
# values as arguments. This will output a list of random strings with the
# specified length and number of strings.