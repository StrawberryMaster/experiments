# Script to calculate the distance between two coordinates on Earth in km.
# Lightly edited - @source https://github.com/Sohum09/Code-for-storms/blob/main/DistanceCalculator.py
import math

# Take inputs, converting them to radians in the process:
def get_coordinates():
    print("Enter the coordinates below! Use negatives for southern latitudes and WHEM longitudes.")
    print("\nx here is latitude, y here is longitude.")
    x1 = float(input("x1 in degrees = ")) * 0.0174533
    y1 = float(input("y1 in degrees = ")) * 0.0174533
    x2 = float(input("x2 in degrees = ")) * 0.0174533
    y2 = float(input("y2 in degrees = ")) * 0.0174533
    return x1, y1, x2, y2

# Apply the equation:
def calculate_distance(x1, y1, x2, y2):
    radius = 6378.137  # Assumed radius of the planet
    delY = y2 - y1
    d_km = radius * math.acos(
        math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(delY)
    )
    return d_km

# Finding the equivalent in nautical miles
def convert_to_nautical_miles(d_km):
    return d_km * 0.539957

# Print the output:
def main():
    x1, y1, x2, y2 = get_coordinates() 
    d_km = calculate_distance(x1, y1, x2, y2)
    d_nm = convert_to_nautical_miles(d_km)
    print(f"Distance in km: {d_km:.2f} km, in nautical miles: {d_nm:.2f} nm")

if __name__ == "__main__":
    main()