# This program simulates a mini ATM.
# @author: Ashton Coplin

def main():
    balance = 1500
    choice = ""
    
    while choice != "E":
        choice = getMenuChoice() #Update choice with user input
        
        #Inputs user choice and executes correlating lines of code
        if choice == "W":
            withdrawalAmount = float(input("Enter a withdrawal amount: $"))
            if withdrawalAmount < 1:
                print("Improper withdraw amount entered.\n")
            elif withdrawalAmount > balance:
                print("Insufficient funds.\n")
            else:
                print(f"Please take your ${withdrawalAmount:,.2f}\n")
                balance -= withdrawalAmount #Update balance
                
        elif choice == "D":
            depositAmount = float(input("Enter deposit amount: $"))
            if depositAmount < 1:
                print("Improper deposit amount entered.\n")
            else:
                balance += depositAmount #Update balance
        elif choice =="B":
            print(f"Current balance: ${balance:,.2f}\n")
        
    print("\nThank you for banking with us.")
        
            
        
        
# getMenuChoice presents a banking menu of choices
# @return The customer's menu choice as a single upper
# case letter.

def getMenuChoice():
    print("====================")
    print("Enter W for Withdraw")
    print("Enter D for Deposit")
    print("Enter B for Balance")
    print("Enter E for Exit")
    print("====================")
    choice = str(input("Choice: ")).upper()
    return choice
    
main()