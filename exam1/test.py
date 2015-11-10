
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

