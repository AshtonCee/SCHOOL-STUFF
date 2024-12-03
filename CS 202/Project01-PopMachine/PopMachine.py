# This program runs a simple pop machine.
# @author Ashton Coplin
from Slot import Slot
from Soda import Soda

def main():
    popMachine = startMachine("sodas.txt")
    purchaseMore = "Y"
    while (purchaseMore[0].upper() == "Y"):
        showMachine(popMachine)
        slotNum = int(input("Which slot #? "))

        # ** ADD CODE **
        # Remember that the index of the slot in the machine is
        # 1 less than slotNum just entered by the user above.
        item = popMachine[slotNum - 1].getItem()  # Get the item directly
        quantity = popMachine[slotNum - 1].getQuantity()  # Get the quantity directly
        slot = Slot(item, quantity)  # Create a new Slot

        if slot.getQuantity() == 0:
            print(f"Slot {slotNum} sold out.")
        else:
            initialDeposit = 0
            while initialDeposit < slot.getItem().getPrice():
                initialDeposit += float(input("Enter deposit: $"))
                if initialDeposit >= slot.getItem().getPrice():
                    print(f"Please take your {slot.getItem().getName()}.")
                    slot.purchase(1)
                    popMachine[slotNum - 1].setQuantity(slot.getQuantity())
                    change = initialDeposit - slot.getItem().getPrice()
                    if change > 0:
                        print(f"Your change is ${change:.2f}.")
                    
                else:
                    print(f"Enter ${slot.getItem().getPrice() - initialDeposit:.2f} more.")


        # If the slot's quantity is 0 
        #   state that the slot is sold out (Remember to match the output)
        # else 
        #   1. Continue to get deposits until enough money is entered
        #   2. Tell the user to take their soda. Telling them to take
        #   their change if some is left is optional. This was not done
        #   in the sample run.
        #   3. Call the purchase method for the slot with a value of 1.
        #      (This means that 1 item was purchased from the slot)


        purchaseMore = input("Purchase another item (Y or N)? ")
        print()
    stopMachine(popMachine, "sodasChanged.txt")

# startMachine stocks the pop machine based upon file data
# @param filename The filename containing the data
# @return A pop machine list filled with slots
def startMachine(filename):
    machine = []
    with open(filename, "r") as inFile:
        for line in inFile:
            slotData = line.split(",")
            soda = Soda(slotData[0], 
                        float(slotData[1]),
                        int(slotData[2]))
            slot = Slot(soda, int(slotData[3]))
            machine.append(slot)
    return machine

# showMachine shows the sodas in the machine, preceded with a slot
# number. The quantity in the slot is also shown.
# @param machine The list of pop machine slots
def showMachine(machine):
    slotNum = 1
    for slot in machine:
        soda = slot.getItem()
        print(f"{slotNum}. {soda.getName()}, ${soda.getPrice():.2f}" +
              f" ({slot.getQuantity()} available)")
        slotNum += 1

# stopMachine stores the current state of the machine back to file
# @param machine The list of pop machine slots
# @param filename The filename to which the data is written
def stopMachine(machine, filename):
    with open(filename, "w") as outFile:
        for slot in machine:
            outFile.write(f"{slot}\n")
            
main()