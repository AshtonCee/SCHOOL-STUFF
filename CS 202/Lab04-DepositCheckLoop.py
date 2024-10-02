# This program processes bank account checks and prevents a negative balance.
# @author: Ashton Coplin

balance = float(input("Please enter a balance: $"))
checkAmount = 1

# Loop until the checkAmount is non-positive or the balance becomes 0
while checkAmount > 0 and balance > 0:
    print()
    checkAmount = float(input("Check amount (0 or negative to end): $"))
    
    if checkAmount > balance:
        print("Warning: Check will bounce. No transaction occurred.")
    elif checkAmount > 0:
        balance -= checkAmount
        print(f"Current balance: ${balance:.2f}")
    # Terminate the loop if checkAmount is negative or 0

# Print the final balance after the loop terminates
print(f"\nFinal balance: ${balance:.2f}")