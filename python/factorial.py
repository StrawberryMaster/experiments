def factorial(n):
  # Base case: n = 0
  if n == 0:
    return 1
  
  # Recursive case: n > 0
  else:
    return n * factorial(n - 1)

# Test the function
print(factorial(5)) # Should print 120
print(factorial(0)) # Should print 1
print(factorial(1)) # Should print 1
print(factorial(10)) # Should print 3628800

# We defines a function called factorial that calculates the factorial
# of a given number n. The factorial of a number is the product of all
# the positive integers from 1 up to that number. For example, the
# factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
#
# The factorial function uses recursion to calculate the factorial. It has two cases:
## If n is 0, the function returns 1 (the base case).
## If n is greater than 0, the function returns n multiplied by the factorial of n - 1.