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
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_car_values(door_amount)):
            self._vehicle_list.append(item.Car(door_amount,maker, model,price, year))
        else:
            print("values entered are not accepted")
        print(self._vehicle_list[0])
        
    def add_sm(self, maker, model, price, year, seat_amount, reverse):
        """ this method adds a snowmobile to the vehicle_list if all teh valeus
        are correct and acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_sm_values(seat_amount, reverse)):
            self._vehicle_list.append(item.Snowmobile(seat_amount, reverse,maker, model,price, year))
        else:
            print("values entered are not accepted")
        
        