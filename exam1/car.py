import item


class Car(Item):
    """ This class describes which attributes the car shall have"""
    
    def __init__(self, door_amount, maker, model, price, year):
        """ the constructor calls the super class init function 
            with the arguments maker, model, price and year as arguments
            it then sets the type to car and the door amount to the argument door_amount"""
        
        super().__init__(maker, model, price, year)
        
        self._type = "car"
        self.door_amount = door_amount
        
        
    