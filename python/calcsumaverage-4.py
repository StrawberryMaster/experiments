def calc_sum_and_avg(number1, number2):
    # Calculate the sum and average
    sum = number1 + number2
    average = sum / 2

    # Return the results as a tuple
    return sum, average

def main():
    # Read the two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Call the calc_sum_and_avg() function and unpack the results
    sum, average = calc_sum_and_avg(number1, number2)

    # Print the results
    print(f"The sum of {number1} and {number2} is: {sum}")
    print(f"The average of {number1} and {number2} is: {average:.2f}")

# Call the main() function
if __name__ == "__main__":
    main()

# In this example, we define a function calc_sum_and_avg() that
# takes two numbers as arguments and returns their sum and average
# as a tuple. We then define a main() function that reads the two
# numbers from the user, calls the calc_sum_and_avg() function,
# and prints the results.
##
# We use the if __name__ == "__main__": block to ensure that the
# main() function is only called when the program is run directly,
# rather than when it is imported by another script. This is a common
# pattern in Python programs that helps to prevent code in the script
# from being executed unnecessarily.