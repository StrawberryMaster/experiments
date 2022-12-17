# Define the two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the sum and average
sum = number1 + number2
average = sum / 2

# Print the results
print("The sum of the two numbers is: {:.2f}".format(sum))
print("The average of the two numbers is: {:.2f}".format(average))

# In this example, we use the input() function to read
# the two numbers from the user. We use the float() function
# to convert the input strings to floating point numbers.
# We then calculate the sum and average as before, and use the
# format() method to include the values of the variables sum
# and average in the output string.