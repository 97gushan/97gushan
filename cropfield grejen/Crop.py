# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:02:24 2015

@author: 97gushan
"""

class Crop:
    """ This is a generic food crop """
    
    def __init__(self, growth_rate, light_need, water_need):
        """ constructor --- creats variables and give them a value"""

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "generic"
        
        
    def needs(self):
        """ returns the value of light_need and water_need in a dictionary"""
        
        return {'light need': self._light_need, 'water need': self._water_need}
        
    def report(self):
        """ this method provides an overview of the Crop-class,
        it returns the values of type, status, growth, days_growing in a dictionary"""
        
        return {'type': self._type, 'status': self._status,\
                'growth': self._growth, 'days growing': self._days_growing}
                
    # get methods
                
                
    def get_growth(self):
        """this method returns the value of self._growth as a int"""
        return self._growth        
        
    def get_days_growing(self):
        """ this method returns the value of self._days_growing as a int"""
        return self._days_growing        
        
    def get_growth_rate(self):
        """ this method returns the value of self._growth_rate as a float"""
        return self._growth_rate
    
    def get_light_need(self):
        """ this method returns the value of self._light_need as a int"""
        return self._light_need
        
    def get_water_need(self):
        """ this method return the vallue of self._watrer_need as a float"""
        return self._water_need        
        
    def get_status(self):
        """ this method returns the value of self._status as a string"""
        return self._status
    
    def get_type(self):
        """ this method rreturns the value of self._type as a string"""
        return self._type
        
    
    # set methods
    
    def set_growth(self, growth):
        """ this method takes a int as an argument and sets self._growth to that value"""
        self._growth = growth
        
    def set_days_growing(self, days):
        """ this method takes a int as an argument and sets self._days_growing to that value"""
        self._days_growing = days
        
    def set_growth_rate(self, rate):
        """ this method takes a float as an argument and sets self._growth_rate to that value"""
        self._growth_rate = rate
        
    def set_light_need(self, light):
        """ this method takes a int as an argument and sets self._light_need to that value"""
        self._light_need = light
    
    def set_water_need(self, water):
        """ this method takes a float as an argument and sets self._water_need to that value"""
        self._water_need = water
        
    def set_status(self, status):
        """ this method takes a string as an argument and sets self._status to that value"""
        self._status = status
        
    def set_type(self, new_type):
        """ this method takes a string as an argument and sets self._type to that value"""
        self._type = new_type
        
        
def main():
    # instantiate the Crop class 
    crop = Crop(1,2,3)
    
    #print out some stuff
    print(crop.needs())
    
if(__name__ == "__main__"):
    main()