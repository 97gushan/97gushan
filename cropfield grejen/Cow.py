from Animal import *

class Cow(Animal):
    """ A cow class"""
    
    def __init__(self):
        
        super().__init__(5, 5, 4, 3, "cow")
        
        self._type = "cow"
        
        
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
    # create a cow animal object
    cow_animal = Cow()
    print(cow_animal.report())
    
    # manually grow the crop
    manual_grow(cow_animal)
    
    print(cow_animal.report())
    
    manual_grow(cow_animal)
    
    print(cow_animal.report())
    
    
if __name__ == "__main__":
    main()
