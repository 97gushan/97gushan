from Animal import *

class Pig(Animal):
    """ A pig class"""
    
    def __init__(self):
        
        super().__init__(3, 6, 2, 2, "pig")
        
        self._type = "pig"
        
        
    def grow(self, food, water):
        """ override the grow function"""
        
        if(food >= self._food_need and water >= self._water_need):
            if(self._status == "baby" and water > self._water_need):
                self._weight += self._growth_rate * 1.5
            elif(self._status == "youngling" and water > self._water_need):
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
                
        # increament day growing
        self._days_growing += 1
        #update status
        self._update_status()
        
        
def main():
    # create a pig animal object
    pig_animal = Pig()
    print(pig_animal.report())
    
    # manually grow the crop
    manual_grow(pig_animal)
    
    print(pig_animal.report())
    
    manual_grow(pig_animal)
    
    print(pig_animal.report())
    
    
if __name__ == "__main__":
    main()
