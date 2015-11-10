import test
import item


class Model: 
    
    def __init__(self):
        
        self._vehicle_list = [] 
        
        self.test_object = test
        
        #self.add_vehicle_through_command()
        self.add_car("audi", "a8", "1000", "1990","2")
        
        
        
        
    def add_car(self, maker, model,price, year, door_amount):
        """ this method adds a car to the vehicle_list if all the values
        are acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year)):
            self._vehicle_list.append(item.Car(door_amount,maker, model,price, year))
        print(self._vehicle_list[0])
        
        