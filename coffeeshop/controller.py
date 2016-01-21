from insert_product_data import * 
from delete_existin_product import * 
from database import * 
from update_database import * 
from select_existing_products import * 
from insert_data_relationships import * 
from get_information_from_db import *

def customer_controll():
    while(True):
        print("\n")
        print("1. (Re)create customer table")
        print("2. Add customer")
        print("3. Remove customer")
        print("4. Print customer details")
        print("5. Print all customer details")
        print("")
        print("0. Return to main menu\n")
        
        
        user_choice = input("Please select an option: ")
        
        
        if(user_choice == "1"):
            create_customer_table(db_name)
        elif(user_choice == "2"):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            Street = input("Enter street: ")
            Town = input("Enter town: ")
            PostCode = int(input("Enter postal code: "))
            TelephoneNumber = int(input("Enter phone number: "))
            EMailAdress = input("Enter email: ")
            
            insert_customer_data((first_name,last_name,Street,Town,PostCode,TelephoneNumber,EMailAdress))
            
        elif(user_choice == "3"):
            ID = int(input("ID of customer to remove: "))
            delete_customer((ID,))
            
        elif(user_choice == "4"):
            ID = int(input("ID of customer to get information about: "))
            get_customer_information(ID)
        
        elif(user_choice == "5"):
            get_all_customer_info()
            
        if(user_choice == "0"):
            break

def product_type_controll():
    while(True):
        print("\n")
        print("1. (Re)create ProductType table")
        print("2. Add product type")
        print("3. Remove product type")
        print("4. Print product type details")
        print("5. Print all product type details")
        print("")
        print("0. Return to main menu\n")
        
        
        user_choice = input("Please select an option: ")
        
        if(user_choice == "1"):
            create_product_type_table(db_name)
        elif(user_choice == "2"):
            Description = input("Product type description: ")
            
            insert_product_type_data((Description,))
            
        elif(user_choice == "3"):
            ID = int(input("ID of product type to remove: "))
            delete_product_type((ID,))
            
        elif(user_choice == "4"):
            ID = int(input("ID of product type to get information about: "))
            get_product_type_information(ID)
        
        elif(user_choice == "5"):
            get_all_product_type_info()
        
        if(user_choice == "0"):
            break

            
def main_controlls():    
    while(True):
        print("\n\n")
        print("1. Customer controlls")
        print("5. Product type controlls")
        print("0. Exit")


        user_choice = input("Please select an option: ")
        
        if(user_choice == "1"):
            customer_controll()
        elif(user_choice == "5"):
            product_type_controll()
        elif(user_choice == "0"):
            break
            
if(__name__ == "__main__"):
    db_name = "coffe_shop.db"
    main_controlls()