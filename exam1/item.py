
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
        
        
        
        
        