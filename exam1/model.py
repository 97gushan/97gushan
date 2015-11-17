import test
import item


class Model: 
    
    def __init__(self):
        
        self._vehicle_list = [] 
        
        self.test_object = test
        
        #self.add_vehicle_through_command()
        self.add_sm("audi", "a8", "1000", "1990","2", True)
        self.add_car("opel", "5", "9999", "1950", "4")

        self.write_to_file()
        self.read_from_file()
        #self.write_to_file()
        
        
        
    def add_car(self, maker, model,price, year, door_amount):
        """ this method adds a car to the vehicle_list if all the values
        are acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_car_values(door_amount)):
            
            # add car to vehicle_list
            self._vehicle_list.append(item.Car(maker, model,price, year,door_amount))
        else:
            print("values entered are not accepted")
        print(self._vehicle_list[0])
        
    def add_sm(self, maker, model, price, year, seat_amount, reverse):
        """ this method adds a snowmobile to the vehicle_list if all teh valeus
        are correct and acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_sm_values(seat_amount, reverse)):
            
            # add snowmobile to vehicle_list
            self._vehicle_list.append(item.Snowmobile(maker, model,price, year,seat_amount, reverse))
        else:
            print("values entered are not accepted")
        
        #print(self._vehicle_list[0])
        
        
    def remove_vehicle(self, index):
        """ this method takes a int as an argument and
        removes the object from vehicle_list with that index"""
        self._vehicle_list.pop(index)
        
        
        
    def get_vehicle_list(self):
        """ this method returns the vehicle list"""
        return self._vehicle_list

        
    def set_car_values(self, index, maker, model, price, year, door_amount):
        """ this method sets new values to a car object"""
        
        # check so the values are acceptable
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_car_values(door_amount)):
            
            # set the new values to the object
            self._vehicle_list[index].set_maker(maker)
            self._vehicle_list[index].set_model(model)
            self._vehicle_list[index].set_price(price)
            self._vehicle_list[index].set_year(year)
            self._vehicle_list[index].set_door_amount(door_amount)
            
    def set_sm_values(self, index, maker, model, price, year, seat_amount, reverse):
        """ this method sets new values to a snowmobile object"""
        
        # check so the values are acceptable
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_sm_values(seat_amount, reverse)):
            
            # set the new values to the object
            self._vehicle_list[index].set_maker(maker)
            self._vehicle_list[index].set_model(model)
            self._vehicle_list[index].set_price(price)
            self._vehicle_list[index].set_year(year)
            self._vehicle_list[index].set_seat_amount(seat_amount)
            self._vehicle_list[index].set_reverse(reverse)
        
    def write_to_file(self):
        """ this method writes to the file"""
        file = open("./vehicles.csv", 'w')
        
        for item in self._vehicle_list:
            file.write(item.__str__())
        
        file.close()
        
        
        
    def read_from_file(self):
        """ this method reads from the vehicle file and 
            creates objects with those values and adds them 
            to the vehicle_list"""
            
        file = open("./vehicles.csv", "r")
        
        self._vehicle_list = []
        
        for line in file:
        
            # removes unnecesary spaces
            line.split()
            
            values = line.split(";")
            
            ##############################
            # must remove the \n in the last value 
            last_value = values[len(values)-1]
            last_value = last_value.rstrip("\n")
            print(last_value)
            print("test")
            
            # check if it should be a car
            if(values[0] == "car"):
            
                # add the vehicle to the list
                self._vehicle_list.append(item.Car(values[1], values[2], values[3], values[4],last_value))
            
            # check if it should be a snowmobile
            elif(values[0]== "snowmobile"):
                
                # add the vehicle to the list
                self._vehicle_list.append(item.Snowmobile(values[1], values[2], values[3], values[4], values[5], last_value))
            
        
        
        file.close()