from Potato import *
from Wheat import *
from Pig import *
from Cow import *

import random

class Field:
    """ simulate a field that contain animals and crops"""
    
    def __init__(self, max_animals, max_crops):
        
        self._crops = []
        self._animals = []        
        self._max_animals = max_animals
        self._max_crops = max_crops
        
    def plant_crop(self, crop):
        """ this method takes a crop object as a atribute. It checks if 
            the amount of crops is less then the max crops. If it is not
            add a crop """
        if(len(self._crops) < self._max_crops):
            self._crops.append(crop)
            return True
        else:
            return False
    
    def add_animal(self, animal):
        """ this method takes an animal object as a atribute. It checks if 
            the amount of animals is less then the max animals. If it is not
            add a animal """
        if(len(self._animals) < self._max_animals):
            self._animals.append(animal)
            return True
        else:
            return False
    
    def harvest_crop(self, index):
        """ this method removes the crop at the chosen index from the list
        and returns the value"""
        if(len(self._crops) > 0):
            return self._crops.pop(index)
    
    def slaughter_animal(self, index):
        """ this method removes the animal at the chosen index from the list
        and returns the value"""
        if(len(self._animals) > 0):
            return self._animals.pop(index)
            
    def report_contents(self):
        """ this method creates two lists with the values from crop.report()
        and aniimal.report(), then the two lists are returned"""
        crop_report = []
        animal_report = []
        
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        
        return {"crops": crop_report, "animals": animal_report}


    def report_needs(self):
        """ this method checks the amount of light, water and food that is
        needed and then it returns the values"""
        food = 0
        light = 0
        water = 0
        
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        
        for animal in self._animals:
            needs = animal.needs()
            
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]
        return {"food": food, "light": light, "water": water}

    def grow(self, light, food, water):
        """ this method grows the crops and animals with 
            the water, food and light that is avaible"""
        
        # grows the crops (water and light is avaible to all 
        # the crops in the same amount)        
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)
        
        # grows the animals ( water is avaible to all animals in the same amount)
        # food have a total value and must be shared
        if(len(self._animals) > 0):
            food_required = 0
            # get a total of the food required by the animals
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["food need"]
            
            # if we have more food available than is required work out the 
            # additional available food
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
                
            # grow the animals
            for animal in self._animals:
                needs = animal.needs()
                if food >= needs["food need"]:
                    # remove food this animal eats
                    food -= needs["food need"]
                    feed = needs["food need"]
                    # see if there is any additional food to give
                    if additional_food > 0:
                        #remove some additional food for this animal
                        additional_food -= 1
                        
                        feed += 1
                        
                    #grow the animal
                    animal.grow(feed, water)

def auto_grow(field, days):
    # this function grows the field over x days,
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)    

def manual_grow(field):
    # get the light, water and food values from the user and grow the field
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value: "))
            
            if 1 <= light <= 10:
                valid = True
            else:
                print("Entered value is not valid")
        except ValueError:
            print("Entered value is not valid")
        
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value: "))
            
            if 1 <= water <= 10:
                valid = True
            else:
                print("Entered value is not valid")
        except ValueError:
            print("Entered value is not valid")
    
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value:"))
            
            if 1 <= food <= 100:
                valid = True
            else:
                print("Entered value is not valid")
        except ValueError:
            print("Entered value is not valid")
    
    #grow the field
    field.grow(light, water, food)

def display_crops(crop_list):
    """ this function displays the crops in the field"""    
    
    print()
    print("The following crops are in this field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos, crop.report()))
        pos += 1
        

def display_animals(animal_list):
    """ this function prints out the animals on the field"""
    print()
    print("The following animals are in this field")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos, animal.report()))
        pos += 1

def select_crop(length_list):
    """ this function returns the index of the chosen crop"""
    valid = False
    
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1, length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected -1
    
def select_animal(length_list):
    """ this function returns the index of the chosen animal"""
    valid = False
    
    while not valid:
        selected = int(input("Please select a animal: "))
        if(selected in range(1, length_list+1)):
            valid = True
        else:
            print("Please select a valid option")
    return selected -1
    

def harvest_crop_from_field(field):
    """ this function removes a crop from the field and returns the value"""
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)
    
def slaughter_animal_from_field(field):
    """ this function removes a animal from the field and returns the value"""
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.slaughter_animal(selected_animal)

def display_crop_menu():
    print()
    print("Wich crop type would you like to add?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. I don't want to add a crop - return to main menu")
    print()
    print("Please select a value: ")
    
def display_animal_menu():
    print()
    print("Wich animal would you like to chose?")
    print()
    print("1. Cows")
    print("2. Pigs")
    print()
    print("0. I don't want to add a animal - return to main menu")
    print()
    print("Please select an option: ")
    
def display_main_menu():
    print()
    print("1. Plant a new crop")
    print("2. Harvest a crop")
    print()
    print("3. Add an animal")
    print("4. Remove an animal")
    print()
    print("5. Grow field manually over a day")
    print("6. Grow field automatically over 30 days")
    print()
    print("7. Report field status")
    print()
    print("8. Exit test program")
    print()
    print("Please select an option: ")

def get_menu_choice(lower, upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice
    
def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    
    if(choice == 1):
        if field.plant_crop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
        
    elif(choice == 2):
        if field.plant_crop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - wheat not planted")
            print()

def plant_animal_in_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    
    if(choice == 1):
        if field.add_animal(Cow()):
            print()
            print("Animal added")
            print()
        else:
            print()
            print("Field is full - cow not added")
            print()
        
    elif(choice == 2):
        if field.add_animal(Pig()):
            print()
            print("Animal added")
            print()
        else:
            print()
            print("Field is full - pig not added")
            print()

def manage_field(field):
    print("Thsi is the field managent program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print()
        if(option == 1):
            plant_crop_in_field(field)
        elif(option == 2):
            remove_crop = harvest_crop_from_field(field)
            print("You removed the crop: {0}".format(remove_crop))
        elif(option == 3):
            add_animal_to_field(field)
        elif(option == 4):
            removed_animal = removed_animal_from_field(field)
            print("You removed  the animal: {0}".format(removed_animal))
        elif(option == 5):
            manual_grow(5)
        elif(option == 6):
            auto_grow(field, 30)
        elif(option ==7):
            print(field.report_contents())
            print()
        elif(option == 0):
            exit = True
            print()
            
    print("Tank you 4 using this shit")
      

def main():
    new_field = Field(5,2)
    
    manage_field(new_field)
    
    
if(__name__ == "__main__"):
    main()