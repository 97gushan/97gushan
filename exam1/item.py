
class Item:
    """ this is the super class that the different items
        are going to use"""
        
    def __init__(self, maker, model, price, year):
        """ Constructor, sets the attributes all the items shall have"""
        
        self._maker = maker
        self._model = model
        self._price = price
        self._year = year
        
    
    """ get methods """
    
    def get_maker(self):
        """ this method returns the value of the string _maker"""
        return self._maker
        
    def get_model(self):
        """ this method returns the value of the string _model"""
        return self._model
        
    def get_price(self):
        """ This method returns the value of the int _price"""
        return self._price
        
    def get_year(self):
        """ this method returns the value of the int _year"""
        return self._year = year
        
    
    """ Set methods """
        
    def set_maker(self, maker):
        """ this method takes a string as an argument 
            and sets the value of _maker to that string"""
        self._maker = maker
        
    def set_model(self, model):
        """ this method takes a string as an argument
            and sets the value of _model to that string"""
        self._model = model
        
    def set_price(self, price):
        """ this method takes an int as an argument
            and sets the value of _price to that int"""
        self._price = price
        
    def set_year(self, year):
        """ this method takes an int as an argument 
            and sets the value of _year to that int"""
        self._year = year
        
        
        

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
        
        
        
        
        
        
        