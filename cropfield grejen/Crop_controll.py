from Wheat import *
from Potato import *
from Pig import *
from Cow import *


def display_menu():
    print()
    print("Wich crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print("3. Pig")
    print("4. Cow")
    print()
    print("Please select an option")
    
def select_option():
    valid_option = False
    
    while not valid_option:
        try:
            choice = int(input("Option slected: "))
            if choice in (1,2,3,4):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if(choice == 1):
        new_crop = Potato()
        
    elif(choice == 2):
        new_crop = Wheat()
    elif(choice == 3):
        new_crop = Pig()
    elif(choice == 4):
        new_crop = Cow()
        
    return new_crop
    
def main():
    new_crop = create_crop()
    manage_crop(new_crop)
    
if __name__=="__main__":
    main()