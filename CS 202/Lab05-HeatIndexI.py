# This program calculates the heat index based on the temperature and humidity.
# @author: Ashton Coplin

# Calculates HeatIndex and returns the value.
def getHeatIndex(temp, humidity):
    HeatIndex = (-42.379 + 2.04901523 * temp + 10.14333127 * humidity - 0.22475541 * temp * humidity
                 -6.83783 * pow(10, -3) * pow(temp, 2) - 5.481717 * pow(10, -2) * pow(humidity, 2)
                 + 1.22874 * pow(10, -3) * pow(temp, 2) * humidity + 8.5282 * pow(10, -4) * temp * 
                 pow(humidity, 2) - 1.99 * pow(10, -6) * pow(temp, 2) * pow(humidity, 2))
    
    return HeatIndex


def main():
    minTemp = 80
    maxTemp = 110
    minHumidity = 40
    maxHumidity = 100
    userTemp = 0
    userHumidity = 0
    
    while userTemp < minTemp or userTemp > maxTemp:
        userTemp = int(input("Fahrenheit Temperature (" + str(minTemp) + " - " + str(maxTemp) + "): "))
        
    while userHumidity < minHumidity or userHumidity > maxHumidity:
        userHumidity = int(input("Relative Humidity (" + str(minHumidity) + " - " + str(maxHumidity) + "): "))
        
    getHeatIndex(userTemp, userHumidity)
    
    print(f"Heat Index: {getHeatIndex(userTemp, userHumidity):.1f}")
    
    
main()