# This program computes income taxes, using a simplified tax schedule.
# @author: Ashton Coplin

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0
# Read income and marital status
income = float(input("Income: $"))
maritalStatus = input("Enter s for single, m for married: ").lower()
# Compute taxes due.
tax1 = 0 # tax due at first tax bracket income level
tax2 = 0 # remaining tax due if exceeding the first bracket income
if maritalStatus == "s" :
    if income <= (RATE1_SINGLE_LIMIT/4) :
        tax1 = income * RATE1
    elif income <= RATE1_SINGLE_LIMIT : 
        tax1 = (RATE1_SINGLE_LIMIT/4) * RATE1
        tax2 = (income - RATE1_SINGLE_LIMIT/4) * RATE2
    else :
        tax1 = (RATE1_SINGLE_LIMIT/4) * RATE1
        tax2 = (RATE1_SINGLE_LIMIT - (RATE1_SINGLE_LIMIT/4)) * RATE2 + (income - RATE1_SINGLE_LIMIT) * RATE3
elif maritalStatus =="m" :
    if income <= RATE1_MARRIED_LIMIT/4 :
        tax1 = RATE1 * income
    elif income <= RATE1_MARRIED_LIMIT :
        tax1 = (RATE1_MARRIED_LIMIT/4) * RATE1
        tax2 = (income - RATE1_MARRIED_LIMIT/4) * RATE2
    else:
        tax1 = (RATE1_MARRIED_LIMIT/4) * RATE1
        tax2 = (RATE1_MARRIED_LIMIT - (RATE1_MARRIED_LIMIT/4)) * RATE2 + (income - RATE1_MARRIED_LIMIT) * RATE3
else :
    print("Unrecognized marital status")
    tax1 = 0
    tax2 = 0


totalTax = tax1 + tax2
# Display the tax.
if totalTax != 0 :
    print(f"The tax is ${totalTax:,.2f}")