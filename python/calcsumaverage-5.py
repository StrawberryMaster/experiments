def calc_sum_and_avg(numbers):
    # Calculate the sum and average
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)

    # Return the results as a tuple
    return sum, average

def main():
    # Read the two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Create a list of the two numbers
    numbers = [number1, number2]

    # Call the calc_sum_and_avg() function and unpack the results
    sum, average = calc_sum_and_avg(numbers)

    # Print the results
    print(f"The sum of {number1} and {number2} is: {sum}")
    print(f"The average of {number1} and {number2} is: {average:.2f}")

# Call the main() function
if __name__ == "__main__":
    main()

# In this example, we define a function calc_sum_and_avg() that
# takes a list of numbers as an argument and returns their sum
# and average as a tuple. We then define a main() function that
# reads the two numbers from the user, creates a list of the two
# numbers, and calls the calc_sum_and_avg() function.
##
# We use a for loop to iterate over the list of numbers and
# calculate the sum. We then divide the sum by the length of
# the list to calculate the average.