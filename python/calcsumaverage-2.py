# Get the input from the user
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

# Calculate the sum and average
sum = number1 + number2
average = sum / 2

# Print the results
print(f"The sum of {number1} and {number2} is: {sum}")
print(f"The average of {number1} and {number2} is: {average:.2f}")

# In this example, we use the f-string formatting syntax to
# include the values of the variables number1, number2, sum,
# and average in the output string. We also use the :.2f format
# specifier to print the average variable with two decimal places.