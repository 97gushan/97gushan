import item


class Car(Item):
    """ This class describes which attributes the car shall have"""
    
    def __init__(self, door_amount, maker, model, price, year):
        """ the constructor calls the super class init function 
            with the arguments maker, model, price and year as arguments
            it then sets the type to car and the door amount to the argument door_amount"""
        
        super().__init__(maker, model, price, year)
        
        self._type = "car"
        self._door_amount = door_amount
        
    
    
    """ get methods"""
    
    def get_type(self):
        """ this method returns the type of the object"""
        return self._type
        
    def get_door_amount(self):
        """ this method returns the value of the variable door_amount"""
        return self._door_amount
    
    
    """ set methods"""
    
    def set_door_amount(self, door_amount):
        """ this method takes a int as an argument 
            and sets the door_amount to that value"""
        self._door_amount = door_amount
        
        
        