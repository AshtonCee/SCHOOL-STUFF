# @author Ashton Coplin
def showCountyData(countyNames, countySeats, countyPops):
    for i in range(len(countyNames)):
        print(countyNames[i])
        print(f'  Seat: {countySeats[i]}')
        print(f'  Population: {countyPops[i]:,}')
        
def linearSearch(countyNames, name):
    for i in range(len(countyNames)):
        if countyNames[i].lower() == name.lower():
            return i
    return -1

# findInsertionIndex finds the index where value is to be inserted
# into the list.
# @precondition The list of values is in increasing sorted order
# @param theList The list of values
# @param value the value to insert
# @return the located index
def findInsertionIndex(theList, value):
    for i in range(len(theList)):
        if value.lower() < theList[i].lower():
            return i
    return len(theList)

def main():
    countyNames = ["Chase", "Crawford", "Ford", "Harper", "Kiowa", 
                   "McPherson", "Norton", "Republic", "Shawnee", "Wabaunsee"]
    
    countySeats = ["Cottonwood Falls", "Girard", "Dodge City", "Anthony", 
                   "Greensburg", "McPherson", "Norton", "Belleville", 
                   "Topeka", "Alma", ]
    
    countyPops = [2572, 38972, 34287, 5485, 2460, 
                  10038, 5459, 4674, 178909, 6877]
    
        
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty to insert: ").title()
    seat = input(f"{name} County seat: ")
    pop = int(input(f"{name} County population (digits only): "))
    
    index = findInsertionIndex(countyNames, name)
    
    if index < len(countyNames):
        countyNames.insert(index, name)
        countySeats.insert(index, seat)
        countyPops.insert(index, pop)
    else:
        countyNames.append(name)
        countySeats.append(seat)
        countyPops.append(pop)
    # Call findInsertionIndex to find the index where the county name just
    # entered is to be inserted into the countyNames list. Depending upon
    # the index returned either insert or append the county name, seat,
    # and population into their respective lists.

    
    print()  
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty requiring population adjustment: ").title()
    
    index = linearSearch(countyNames, name)
    
    if index != -1:
        print(f"Current population: {countyPops[index]:,}")
        new_pop = int(input(f"New population (digits only): "))
        countyPops[index] = new_pop
    else:
        print(f"{name} County was not found.")
    # Call linearSearch to find the index where the county just entered is
    # located in the countyNames list. IF the name was found, display the
    # current population with thousands separators and prompt for the new
    # population. Store the new population at the given index in the
    # countyPops list. ELSE display that the county wasn't found.

    
    print()    
    showCountyData(countyNames, countySeats, countyPops)
    
    
main()