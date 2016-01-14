from insert_product_data import * 
from delete_existin_product import * 
from database import * 
from update_database import * 
from select_existing_products import * 

while(True):
    print("\n\n")
    print("1.  (Re)Create Product Table")
    print("2.  Add new Product")
    print("3.  Edit existing product")
    print("4.  Delete existing product")

    user_choice = input("Please select an option: ")
    
    if(user_choice == "1"):
        create_table("Product")
    elif(user_choice == "2"):
        type = input("Type: ")
        price = input("price: ")
        
        insert_data((type,price))
    elif(user_choice == "3"):
        id = input("Product id: ")
        type = input("Type: ")
        price = input("price: ")
        
        update_product((type,price,id))
    elif(user_choice == "4"):
        type = input("Delete type: ")
        
        delete_product((type,))
    
    if(user_choice == "0"):
        break
