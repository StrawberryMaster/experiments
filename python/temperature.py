def fahrenheit_to_celsius(temp_f):
  temp_c = round((temp_f - 32) * (5/9), 2)
  return temp_c

def celsius_to_fahrenheit(temp_c):
  temp_f = round(temp_c * (9/5) + 32, 2)
  return temp_f

# Main program
print("Welcome to the temperature converter!")

while True:
  # Get the conversion type from the user
  conversion_type = input("Enter 'F' to convert from Fahrenheit to Celsius, or 'C' to convert from Celsius to Fahrenheit: ")

  # Check the conversion type
  if conversion_type.upper() == 'F':
    temp_f = float(input("Enter the temperature in Fahrenheit: "))
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f} degrees Fahrenheit is equivalent to {temp_c} degrees Celsius.")
  elif conversion_type.upper() == 'C':
    temp_c = float(input("Enter the temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c} degrees Celsius is equivalent to {temp_f} degrees Fahrenheit.")
  else:
    print("Invalid conversion type. Please try again.")
    
  # Check if the user wants to perform another conversion
  another_conversion = input("Would you like to perform another conversion? Enter 'Y' for yes or 'N' for no: ")
  if another_conversion.upper() != 'Y':
    break

print("Thank you for using the temperature converter!")

# We start by defining two functions: fahrenheit_to_celsius
# and celsius_to_fahrenheit, which convert temperatures between
# the two scales.
#
# We then start a loop that continues until the user decides to exit.
# Within the loop, we then prompt the user to choose which conversion
# they want to perform (either Fahrenheit to Celsius or Celsius to Fahrenheit).
# Then we prompt the user to enter the temperature value, and use the
# appropriate conversion function to perform the conversion.
#
# Finally, we print the result of the conversion and ask the user if they want to
# perform another conversion. If the user enters 'Y', the loop continues and we prompt
# the user for another conversion. If the user enters 'N', the loop breaks and we exit.