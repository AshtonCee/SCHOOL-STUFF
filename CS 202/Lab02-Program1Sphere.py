# This program displays a sphere diameter, surface area, and volume based upong a user-entered radius.  
# @author: Ashton Coplin

import math

# Get the radius
radius = float(input("Sphere radius: "))

# Calculate the diameter
diameter = radius * 2

# Calculate the surface area
surface_area = 4 * math.pi * (radius ** 2)

# Calculate the volume
volume = (4 / 3) * math.pi * (radius ** 3)

# Display the results
print(f"Diameter: {diameter: .2f}")
print(f"Surface area: {surface_area: .2f}")
print(f"Volume: {volume: .2f}")
