from Crop import *

class Wheat(Crop):
    """ A potato crop"""
    
    # constructor
    def __init__(self):
        
        # call the super class constructor
        # with the default value for the potato
        super().__init__(1, 2, 2)
        
        self._type = "Wheat"
    
    # override grow method
    def grow(self, light, water):
        if(light >= self._light_need and water >= self._water_need):
            if(self._status == "seedling" and water > self._water_need):
                self._growth += self._growth_rate * 1.5
            elif(self._status == "young" and water > self._water_need):
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        
        # increament day growing
        self._days_growing += 1
        #update status
        self._update_status()

def main():
    # create a potato crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    
    # manually grow the crop
    manual_grow(wheat_crop)
    
    print(wheat_crop.report())
    
    manual_grow(wheat_crop)
    
    print(potato_crop.report())
    
    
if __name__ == "__main__":
    main()