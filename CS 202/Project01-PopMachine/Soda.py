# Class Soda represents a soda with a name, price, and ounces.
# @author Ashton Coplin
from Item import Item

class Soda(Item):
    def __init__(self, name="", price=0, ounces=0): 
        super().__init__(name, price)
        self.set_ounces(ounces)

    def get_ounces(self):
        return self.ounces
    
    def set_ounces(self, ounces):
        if ounces > 0:
            self.ounces = ounces
        else:
            self.ounces = 0

    def __str__(self):
        return super().__str__() + ", " + str(self.get_ounces()) + " oz"