# This program will get a wind speed in miles per our from a user and display the corresponding damage report. 
# @author: Ashton Coplin

# Get wind speed (integer) from the user in miles per hour.
windSpeed = int(input("Wind speed (MPH): "))

# Decide tornado output based on windSpeed variable.
if windSpeed > 200:
    print("EF-5: Destruction of all infrastructure.")
elif windSpeed >= 166 and windSpeed < 200:
    print("EF-4: Homes leveled, cars thrown around.")
elif windSpeed >= 133 and windSpeed < 166:
    print("EF-3: Entire stories of homes and buildings destroyed, "
          + "trains overturned, cars lifted off the ground.")
elif windSpeed >= 111 and windSpeed < 133:
    print("EF-2: Torn off roofs, mobile homes destroyed, large trees uprooted.")
elif windSpeed >= 86 and windSpeed < 111:
    print("EF-1: Roofs stripped, mobile homes overturned, exterior home damage.")
elif windSpeed >= 65 and windSpeed < 86:
    print("EF-0: Some damage to roofs, siding, and tree branches.")
else:
    print("Likely not a tornado.")