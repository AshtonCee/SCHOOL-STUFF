# This program converts a l ong jump given in centimeters to feet and inches
# @author Ashton Coplin

# Constant variables
cms_per_inch = 2.54
inches_per_feet = 12

# Get the athlete's name and distance jumped
first_name = input("Long jumper's first name: ")
last_name = input("Long jumper's last name: ")

# Get the distance in centimeters
centi = int(input("Distance jumped (cm): "))

# Convert cm to inches
inches = centi/cms_per_inch

# Convert cm to feet
ft = inches/inches_per_feet

# Get inches left over
inches_remainder = inches % inches_per_feet

# Display the results
print(first_name, last_name, "jumped", int(ft), "' - ", inches_remainder, "\"")
