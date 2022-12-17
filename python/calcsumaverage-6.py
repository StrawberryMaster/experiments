def calc_sum_and_avg(numbers):
    # Calculate the sum and average
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)

    # Return the results as a dictionary
    results = {
        "sum": sum,
        "average": average
    }
    return results

def main():
    # Read the two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Create a list of the two numbers
    numbers = [number1, number2]

    # Call the calc_sum_and_avg() function and store the results in a variable
    results = calc_sum_and_avg(numbers)

    # Print the results
    print(f"The sum of {number1} and {number2} is: {results['sum']}")
    print(f"The average of {number1} and {number2} is: {results['average']:.2f}")

# Call the main() function
if __name__ == "__main__":
    main()

# In this example, we define a function calc_sum_and_avg() that
# takes a list of numbers as an argument and returns a dictionary
# containing their sum and average. We then define a main() function
# that reads the two numbers from the user, creates a list of the two
# numbers, and calls the calc_sum_and_avg() function.
#
# We use a for loop to iterate over the list of numbers and
# calculate the sum. We then divide the sum by the length of
# the list to calculate the average.
# 
# We store the results in a dictionary with keys "sum" and "average",
# and return the dictionary from the function. In the main() function,
# we store the results in a variable and access the "sum" and "average"
# values using the dictionary keys.