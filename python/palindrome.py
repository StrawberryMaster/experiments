def is_palindrome(string):
    # Remove non-alphanumeric characters and convert to lowercase
    string = "".join(c for c in string if c.isalnum()).lower()
    # Check if string is a palindrome by comparing to its reversed version
    return string == string[::-1]

def main():
    # Ask the user for the strings they want to check
    strings = input("Enter the strings you want to check, separated by a comma: ").split(',')
    for string in strings:
        # Determine if the string is a palindrome and output the result
        result = "is a" if is_palindrome(string) else "is not a"
        print(f"{string} {result} palindrome.")

if __name__ == "__main__":
    main()

# We are defining a function called "is_palindrome" which takes in a string
# as a parameter. Within the function, we remove all non-alphanumeric characters
# from the string and convert it to lowercase. We then check if the string is a
# palindrome by comparing it to its reversed version.
#
# We then define a main function which asks the user for a list of strings separated
# by a comma. These strings are stored as a list in the variable "strings". We then
# iterate over the list of strings and use the "is_palindrome" function to determine
# if each string is a palindrome. The result is then output to the user.
#
# The script is set up so that the main function is only run if the script is being run
# directly, rather than being imported into another script. This allows us to use the 
# "is_palindrome" function in other scripts without running the main function automatically.