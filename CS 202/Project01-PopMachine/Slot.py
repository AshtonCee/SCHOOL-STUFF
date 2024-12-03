# Class Slot represents a slot in a pop machine that holds an
# item and tracks the quantity in stock
# @author Ashton Coplin
from Item import Item

class Slot:
    def __init__(self, item, quantity=0):
        self.setItem(item)
        self.setQuantity(quantity)

    def __str__(self):
        return str(self.getItem()) + ", " + str(self.getQuantity())

    def purchase(self, amount):
        """
        Deducts the specified amount from the quantity field if the 
        amount is greater than 0 and there is enough quantity.
    
        @param amount The amount to deduct from the quantity
        """
        if amount > 0 and self.getQuantity() >= amount:
            self.setQuantity(self.getQuantity() - amount)

    def setItem(self, newItem):
        self.item = newItem

    def getItem(self):
        return self.item
    
    def setQuantity(self, newQuantity):
        # Only set the quantity if newQuantity can be treated as an integer
        if type(newQuantity) == int:
            self.quantity = newQuantity if newQuantity > 0 else 0
        elif type(newQuantity) == float:
            self.quantity = int(newQuantity) if newQuantity > 0 else 0
        else:
            self.quantity = 0

    def getQuantity(self):
        return self.quantity

