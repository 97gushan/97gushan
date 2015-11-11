import test
import item


class Model: 
    
    def __init__(self):
        
        self._vehicle_list = [] 
        
        self.test_object = test
        
        #self.add_vehicle_through_command()
        self.add_sm("audi", "a8", "1000", "1990","2", True)
        
        
        
        
    def add_car(self, maker, model,price, year, door_amount):
        """ this method adds a car to the vehicle_list if all the values
        are acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_car_values(door_amount)):
            
            # add car to vehicle_list
            self._vehicle_list.append(item.Car(door_amount,maker, model,price, year))
        else:
            print("values entered are not accepted")
        print(self._vehicle_list[0])
        
    def add_sm(self, maker, model, price, year, seat_amount, reverse):
        """ this method adds a snowmobile to the vehicle_list if all teh valeus
        are correct and acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_sm_values(seat_amount, reverse)):
            
            # add snowmobile to vehicle_list
            self._vehicle_list.append(item.Snowmobile(seat_amount, reverse,maker, model,price, year))
        else:
            print("values entered are not accepted")
        
        print(self._vehicle_list[0])
        
        
    def remove_vehicle(self, index):
        """ this method takes a int as an argument and
        removes the object from vehicle_list with that index"""
        self._vehicle_list.pop(index)
        
        
        
    def get_vehicle_list(self):
        """ this method returns the vehicle list"""
        return self._vehicle_list

        