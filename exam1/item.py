
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
        return self._year
        
    
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
        
        
        
#################################################################################################


class Car(Item):
    """ This class describes which attributes the car shall have"""
    
    def __init__(self, maker, model, price, year, door_amount):
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
        
    
    
    def __str__(self):
        """this method returns the attributes of the class in a string"""
        return self._type + ";" + self._maker + ";" + self._model + ";" \
        + self._price + ";" + self._year + ";" + self._door_amount + "\n"
        
        
#################################################################################################

        
class Snowmobile(Item):
    """ This class describes which attributes the snowmobile shall have"""
    
    def __init__(self, maker, model, price, year, seat_amount, reverse):
        """ the constructor calls the super class init function 
            with the arguments maker, model, price and year as arguments
            it then sets the type to car and the door amount to the argument seat_amount 
            and have_reverse"""
        
        super().__init__(maker, model, price, year)
        
        self._type = "snowmobile"
        self._seat_amount = seat_amount
        self._have_reverse = reverse
        
    
    
    """ get methods"""
    
    def get_type(self):
        """ this method returns the type of the object"""
        return self._type
        
    def get_seat_amount(self):
        """ this method returns the value of the variable door_amount"""
        return self._seat_amount
    
    def get_reverse(self):
        """ this method returns the value of have_reverse"""
        return self._have_reverse
    
    """ set methods"""
    
    def set_seat_amount(self, seat_amount):
        """ this method takes a int as an argument 
            and sets the door_amount to that value"""
        self._seat_amount = seat_amount
    
    def set_reverse(self, reverse):
        """ this method takes a boolean as a value and sets
            have_reverse to that value"""
        self._have_reverse = reverse
        
    def __str__(self):
        """this method returns the attributes of the class in a string"""
        
        # check if have_reverse is true
        if(self._have_reverse):
            return_value = "True"
        else:
            return_value = "False"
        
        return self._type + ";" + self._maker + ";" + self._model + ";" + self._price \
        + ";" + self._year + ";" + self._seat_amount + ";" + str(return_value) + "\n"
        
        
        
        
        
        
        