import test
import item


class Model: 
    
    def __init__(self):
        
        self._vehicle_list = [] 
        
        self.test_object = test
        
        #self.add_vehicle_through_command()
        self.add_car("audi", "a8", "1000", "1990","2")
        
    def display_menu(self):
        """ this method displays the different vehicles 
        that the user can chose from"""
        print()
        print("1. car")
        print("2. snowmobile")
        print()
    
    def add_vehicle_through_command(self):
        """ this method adds an object to the vehicle_list
        it also asks for values to the attributes"""
        
        self.display_menu()
        
        
        # ask the user what type of vehicle it is
        valid_option = False
        
        while(not valid_option):
        
            try:
                vehicle_choice = int(input("What type of vehicle are you going to add: "))
            
                if vehicle_choice  in (1,2):
                    valid_option = True
                else:
                    print("enter  a valid number")
            except ValueError:
                print("enter  a valid number")
                
        
        # get the maker and model of the vehicle
        maker = input("Maker: ")
        model = input("Model: ")
        
        
        # get the price of the vehicle
        valid_option = False
        
        while(not valid_option):
            try:
                price = int(input("Price of vehicle in $: "))
                
                # check if the price is above 0
                if(price > 0):
                    valid_option = True
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")
        
        
        # get the year that the vehicle was made from the user
        valid_option = False
        
        while(not valid_option):
            try:
                year = int(input("Year: "))
                
                if(year >= 1900 and year <= 2015):
                    valid_option = True
                else:
                    print("Please enter a year above 1900 and below 2016")
            except ValueError:
                print("Please enter a year above 1900 and below 2016") 


        # if it is a car
        if(type == 1):
            # get the amount of doors the car have from the user
            valid_option = False
            
            while(not valid_option):
                try:
                    door_amount = int(input("Amount of door: "))
                    
                    if(door_amount >= 1 and year <= 10):
                        valid_option = True
                    else:
                        print("Please enter a year above 1 and below 10")
                except ValueError:
                    print("Please enter a year above 1 and below 10")  
        
        
        
        
    def add_car(self, maker, model,price, year, door_amount):
        """ this method adds a car to the vehicle_list if all the values
        are acceptable"""
        
        if(self.test_object.check_item_values(maker,model,price,year)):
            self._vehicle_list.append(item.Car(door_amount,maker, model,price, year))
        print(self._vehicle_list[0])
        
        