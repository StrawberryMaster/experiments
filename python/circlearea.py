import math

def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle: "))

    # validate the radius
    if radius <= 0:
        print("Invalid radius. Radius must be greater than 0.")
        return

    # calculate and display the area of the circle
    area = math.pi * radius**2
    print(f"The area of the circle is {area:.2f}.")

if __name__ == "__main__":
    main()

# The program above calculates the area of a circle based on the radius provided
# by the user. It prompts the user to enter the radius of the circle, and then it
# validates the input to ensure that the radius is greater than 0. If the radius
# is invalid, it displays an error message and exits the program. Otherwise, it
# calculates the area of the circle and displays the result to the user.