
class Item:
    """ this is the super class that the different items
        are going to use"""
        
    def __init__(self, maker, model, price, year):
        """ Constructor, sets the attributes all the items shall have"""
        
        self._maker = maker
        self._model = model
        self._price = price
        self._year = year
        