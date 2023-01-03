def factorial(n, memo={}):
    # Base case: n = 0
    if n == 0:
        return 1

    # Check if the factorial has already been calculated
    if n in memo:
        return memo[n]

    # Recursive case: n > 0
    else:
        result = n * factorial(n - 1, memo)
        memo[n] = result
        return result

# Test the function
n = int(input("Enter a positive integer: "))
print(factorial(n))

# Test the function
#print(factorial(5)) # Should print 120
#print(factorial(0)) # Should print 1
#print(factorial(1)) # Should print 1
#print(factorial(10)) # Should print 3628800

# We defines a function called factorial that calculates the factorial
# of a given number n. The factorial of a number is the product of all
# the positive integers from 1 up to that number. For example, the
# factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
#
# The factorial function uses recursion to calculate the factorial. It has two cases:
## If n is 0, the function returns 1 (the base case).
## If n is greater than 0, the function returns n multiplied by the factorial of n - 1.
#
# Update: this now uses a dictionary called memo to store the results of previously
# calculated factorials. If the factorial of a given number has already been calculated,
# it is retrieved from the memo dictionary and returned. If it has not been calculated yet,
# it is calculated using the recursive case and then stored in the memo dictionary for
# future reference. 