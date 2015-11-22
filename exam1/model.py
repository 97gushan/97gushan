import test
import item


class Model: 
    
    def __init__(self):
        
        self._vehicle_list = [] 
        
        self.test_object = test
        
        
        
    def add_car(self, maker, model,price, year, door_amount):
        """ this method adds a car to the vehicle_list if all the values
        are acceptable"""
        
        # call the test methods to see if the variables entered are acceptable
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_car_values(door_amount)):
            
            # add car to vehicle_list
            self._vehicle_list.append(item.Car(maker, model,price, year,door_amount))
            
            return True
        else:
            print("values entered are not accepted")
            
            return False
        
        
    def add_sm(self, maker, model, price, year, seat_amount, reverse):
        """ this method adds a snowmobile to the vehicle_list if all teh valeus
        are correct and acceptable"""
        
        
        # call the test methods to see if the variables entered are acceptable
        if(self.test_object.check_item_values(maker,model,price,year) and 
        self.test_object.check_sm_values(seat_amount, reverse)):
            
            # add snowmobile to vehicle_list
            self._vehicle_list.append(item.Snowmobile(maker, model,price, year,seat_amount, reverse))
            
            return True
        else:
            print("values entered are not accepted")
            return False
        
        
        
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
            
            return True
        else: 
            return False
            
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
    
            return True
        else: 
            return False
    
    def search_for_object(self, type, search_word):
        """ this method takes two strings as arguments
        then it does a linear search for the objects that have the search_word"""
        
        # create a list to hold the indexes of the found vehicles
        index_list = []
        
        # loop through all the objects in the vehicle_list
        for n in range(len(self._vehicle_list)):
            # if the user wants to search for the maker
            if(type == "maker"):
                # if the maker matches with the searchword
                if(self._vehicle_list[n].get_maker() == search_word):
                    index_list.append(n)
            
            elif(type == "model"):
                if(self._vehicle_list[n].get_model() == search_word):
                    index_list.append(n)
           
            elif(type == "price"):
                if(self._vehicle_list[n].get_price() == search_word):
                    index_list.append(n)
                    
            elif(type == "year"):
                if(self._vehicle_list[n].get_year() == search_word):
                    index_list.append(n)
                    
        
        return index_list
    
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

            
            # check if it should be a car
            if(values[0] == "car"):
            
                # add the vehicle to the list
                self._vehicle_list.append(item.Car(values[1], values[2], values[3], values[4],last_value))
            
            # check if it should be a snowmobile
            elif(values[0]== "snowmobile"):
                
                # add the vehicle to the list
                self._vehicle_list.append(item.Snowmobile(values[1], values[2], values[3], values[4], values[5], last_value))
            
        
        
        file.close()
        
        
    def sort_list(self, type):
        """ this method sorts the vehicle_list when called
            it is sorted by the user chosen category"""
        
        temp_list = []
        index_list = []
        
        # get all the values from the chosen category and the index of those objects
        for n in range(len(self._vehicle_list)):
            
            if(type == "maker"):
                temp_list.append(self._vehicle_list[n].get_maker())
            elif(type == "model"):
                temp_list.append(self._vehicle_list[n].get_model())
            elif(type == "price"):
                temp_list.append(int(self._vehicle_list[n].get_price()))
            elif(type == "year"):
                temp_list.append(int(self._vehicle_list[n].get_year()))
            index_list.append(n)
        
        print(temp_list)
        print(index_list)
        
        # if the type is eitehr price or year do a bubble sort
        if(type == "price" or type == "year"):
            for n in range(len(temp_list)-1, 0, -1):
                
                for m in range(0,n):
                    
                    if(temp_list[m] > temp_list[m+1]):
                        temp_list[m], temp_list[m+1] = temp_list[m+1], temp_list[m]
                        index_list[m], index_list[m+1] = index_list[m+1], index_list[m]
                    
        print()
        print(temp_list)
        print(index_list)
    