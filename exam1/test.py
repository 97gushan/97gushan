
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
    elif(not year.isdigit()):
        is_valid = False
    
    return is_valid
    
def check_car_values(door_amount):
    """ this method takes the door_amount and checks if they
    are an int or not, if yes return true, else, return false"""
    
    
    if(not door_amount.isdigit()):
        return False
    else:
        # check so the door_amount is above 0 and below 10
        if(door_amount > 0 and door_amount <= 10):
            return True
        else:
            return False

