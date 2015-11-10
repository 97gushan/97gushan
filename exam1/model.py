
class Model: 
    
    def __init__(self):
        
        self.vehicle_list = [] 
        
        self.add_vehicle_through_command()
        
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
        
        