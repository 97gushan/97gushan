# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:02:24 2015

@author: 97gushan
"""

class Crop:
    """ Tis is a generic food crop """
    
    def __init__(self, growth_rate, light_need, water_need):
        """ constructor --- creats variables and give them a value"""

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "generic"
        
        
        
def main():
    # instantiate the Crop class 
    crop = Crop(1,2,3)
    
    #print out some stuff
    print(crop._status)
    
if(__name__ == "__main__"):
    main()