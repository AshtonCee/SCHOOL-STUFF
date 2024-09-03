companyList = ["Blizzard", "Rockstar", "Bethesda", "Square Enix", "Ubisoft", "Valve", "Electronic Arts", "Nintendo", "Sega", "Sony", "Microsoft"]
# num of games | num of employees | net worth
companyData = [19, 17000, 74.28], [52, 6400, 22.5], [115, 450, 3], [204, 4712, 4.37], [148, 19410, 2.82], [33, 360, 6.9], [163, 13400, 33.95], [1386, 7317, 56.35], [1027, 3459, 2.73], [1439, 113000, 99.56], [2466, 221000, 2965.64]
    
def menu():
  print("Choose an option: \n1. Display information for ONE company\n2. Display all companies' information.\n3. Compare two companies data\n4. Exit")
  

def displayInformation(companyList, companyData, index):
  if (index >= 0 and index < len(companyList)):
    print("Company: ", companyList[index])
    print("Number of Games: ", companyData[index][0], "games")
    print("Number of Employees: ", companyData[index][1], "employees")
    print("Net Worth: ", companyData[index][2], "billion\n")
  else:
    print("Company not found.\n")
    

def displayAllInformation(companyList, companyData):
  print("Company\t\tNumber of Games\tNumber of Employees\tNet Worth (Billion)")
  for row in range(len(companyList)):
      print("{:<16}".format(companyList[row]), end="")
      for col in range(len(companyData[row])):
          if col == 2:
              print("{:<18.2f}".format(companyData[row][col]), end="")
          else:
              print("{:<20}".format(companyData[row][col]), end="")
      print()
      

def findItem(companyList, companyName):
  for index in range(0, len(companyList)):
    if (companyList[index] == companyName):
      return index
  return -1
  

def compareTwoItems(companyList, companyData):
  company1 = input("Enter the first company name: ").capitalize()
  print()
  index1 = findItem(companyList, company1)
  company2 = input("Enter the second company name: ").capitalize()
  print()
  index2 = findItem(companyList, company2)
  if (index1 >= 0 and index2 >= 0):
    print("Company 1: ", company1)
    print("Number of Games: ", companyData[index1][0], "games")
    print("Number of Employees: ", companyData[index1][1], "employees")
    print("Net Worth: ", companyData[index1][2], "billion\n")
    print("Company 2: ", company2)
    print("Number of Games: ", companyData[index2][0], "games")
    print("Number of Employees: ", companyData[index2][1], "employees")
    print("Net Worth: ", companyData[index2][2], "billion\n")
  else:
    print("Company not found.\n")


def main():
  while True:
    menu()
    print()
    option = int(input("Choose menu option: "))
    print()
    if (option == 1):
      company = input("Enter a company name: ").capitalize()
      index = findItem(companyList, company)
      displayInformation(companyList, companyData, index)
    elif (option == 2):
      displayAllInformation(companyList, companyData)
    elif (option == 3):
      compareTwoItems(companyList, companyData)
    elif (option == 4):
      print("Exiting program...")
      break
    else:
      print("Invalid option. Please try again.")


main()