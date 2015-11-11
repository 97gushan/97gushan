
def check_item_values(maker, model,price, year):
    """ this method takes values as arguments and checks if the 
    first 2 are strings and the second 2 are ints, 
    if everything is correct, return true, else return false"""
    is_valid = True
    
    if(not isinstance(maker, str)):
        is_valid = False
    elif(not isinstance(model, str)):
        is_valid = False
    elif(not price.isdigit()):
        is_valid = False
    elif(int(price) <= 0):
        is_valid = False
    elif(not year.isdigit()):
        is_valid = False
    elif(int(year) < 1990 or int(year) > 2015):
        is_valid = False
    
    return is_valid
    
def check_car_values(door_amount):
    """This method is for the car objects to check the valeus the car have 
    it takes the door_amount and checks if they
    are an int or not, if yes return true, else, return false"""
    
    
    if(not door_amount.isdigit()):
        return False
    else:
        # check so the door_amount is above 0 and below 10
        if(door_amount > 0 and door_amount <= 10):
            return True
        else:
            return False

            
def check_sm_values(seat_amount, reverse):
    """ this method is for checking values that the snowmobiles havethis
        it takes the seat amount as an argument and checks so it is an int
        it also takes reverse and checks so it is a boolean"""
    is_valid = True
    
    if(not seat_amount.isdigit()):
        is_valid = False
    elif(int(seat_amount) <= 0 or int(seat_amount) > 3):
        is_valid = False
    elif(not isinstance(reverse, (bool))):
        is_valid = False
        
    
    return is_valid
    
    
    
