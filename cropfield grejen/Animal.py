
class Animal:
    """ This is a animal class"""
    
    def __init__(self, start_weight, food_need, water_need, growth_rate, name):
        self._weight = start_weight
        self._food_need = food_need
        self._water_need = water_need
        self._growth_rate = growth_rate
        self._days_growing = 0
        self._name = name
        self._status = "baby"
        self._type = ""
        
    def needs(self):
        """ this method returns the needs of the animal"""
        return {"food need":self._food_need, "water need": self._water_need}
        
    def report(self):
        """ this method returns the values of weight, days grown, status and type"""
        return {"status": self._status, "type": self._type,
                "weight": self._weight, "days grown": self._days_growing}
                
    def _update_status(self):
        """ this method updates the status"""
        if(self._weight > 50):
            self._status = "old"
        elif(self._weight > 40):
            self._status = "mature"
        elif(self._weight > 20):
            self._status = "youngling"
        elif(self._weight > 0):
            self._status = "baby"
            
    def grow(self, food, water):
        """ This function grows the animal if the two arguments are more than
            the food and water need"""        
        
        if(food >= self._food_need and water >= self._water_need):
            self._weight += self.get_growth_rate()
        
        # increae amount of days growing
        self._days_growing += 1

        # update the status
        self._update_status()
        
    # get methods
                
                
    def get_weight(self):
        """this method returns the value of self._weight as a int"""
        return self._weight        
        
    def get_days_growing(self):
        """ this method returns the value of self._days_growing as a int"""
        return self._days_growing        
        
    def get_growth_rate(self):
        """ this method returns the value of self._growth_rate as a float"""
        return self._growth_rate
    
    def get_light_need(self):
        """ this method returns the value of self._food_need as a int"""
        return self._light_need
        
    def get_water_need(self):
        """ this method return the vallue of self._water_need as a float"""
        return self._water_need        
        
    def get_status(self):
        """ this method returns the value of self._status as a string"""
        return self._status
    
    def get_type(self):
        """ this method rreturns the value of self._type as a string"""
        return self._type
        
    
    # set methods
    
    def set_weight(self, weight):
        """ this method takes a int as an argument and sets self._weight to that value"""
        self._weight = weight
        
    def set_days_growing(self, days):
        """ this method takes a int as an argument and sets self._days_growing to that value"""
        self._days_growing = days
        
    def set_growth_rate(self, rate):
        """ this method takes a float as an argument and sets self._growth_rate to that value"""
        self._growth_rate = rate
        
    def set_food_need(self, food):
        """ this method takes a int as an argument and sets self._food_need to that value"""
        self._food_need = food
    
    def set_water_need(self, water):
        """ this method takes a float as an argument and sets self._water_need to that value"""
        self._water_need = water
        
    def set_status(self, status):
        """ this method takes a string as an argument and sets self._status to that value"""
        self._status = status
        
    def set_type(self, new_type):
        """ this method takes a string as an argument and sets self._type to that value"""
        self._type = new_type
        

def auto_grow(animal, days):
    """ this function calls the grow method in the animal-object and 
        takes the object and amount of days as arguments"""
    
    for n in range(days):
        # generate new amounts of water and food 
        water = randint(1,10)
        food = randint(1,10)
        
        # call the grow-method 
        animal.grow(food, water)
    
def manual_grow(animal):
    """ this function lets the use chose the amount of water and 
        food that the animal gets during one day"""
    
    valid = False
    
    # check if the food value inputed is a acceptable value
    while(not valid):
        try:
            food = int(input("Please enter a food value (1-10): "))
            
            if( 1 <= food <= 10):
                valid = True
            else:
                print("Value enterterd not valid- please enter a value between 1 and 10")
        except ValueError:
            print("Value enterter not valid - please enter a value between 1 and 10")
            
    valid = False
    
    #check if the water value inputed is a acceptable value
    while(not valid):
        try:
            water = int(input("Please enter a water value (1-10): "))

            if( 1 <= water <= 10):
                valid = True
            else:
                print("Value enterter not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value enterter not valid - please enter a value between 1 and 10")

    animal.grow(food, water)
    
    
def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print("")
    print("Please select an options from the above menu")
    
    
def get_menu_choice():
    option_valid = False
    
    while(not option_valid):
        try:
            choice = int(input("Option select: "))
            
            if(0 <= choice <= 4):
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice
    
def manage_animal(animal):
    print("This is the animal management program")
    print("")
    
    no_exit = True
    
    while(no_exit):
        display_menu()
        option = get_menu_choice()
        print()
        
        if(option == 1):
            manual_grow(animal)
            print()
        elif(option == 2):
            auto_grow(animal, 30)
            print()
        elif(option == 3):
            print(animal.report())
            print()
        elif(option == 0):
            no_exit = False
            print("Thank you for using the test program")
            
            
def main():
    # instantiate the animal class 
    animal = Animal(5,1,2,3, "kalle")
    
    #print out some stuff
    print(animal.report())
    
    manage_animal(animal)
    
if(__name__ == "__main__"):
    main()