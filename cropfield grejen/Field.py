from Potato import *
from Wheat import *
from Pig import *
from Cow import *

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
            needs = crops.needs()
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
    

def main():
    new_field = Field(5,2)
    print(new_field._crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)
    
    new_field.add_animal(Pig())
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Cow())
    
    report = new_field.report_contents()
    print(report)
    
    report = new_field.report_needs()
    print(report)
    
    
if(__name__ == "__main__"):
    main()