import sqlite3

def get_customer_information(id):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Customer where CustomerID=?", (id,))
        customer = cursor.fetchone()
        
        print(customer)
        
def get_all_customer_info():
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Customer")
        customers = cursor.fetchall()
        
        for customer in customers:
            print(customer)
    
    
def get_product_information(id):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product where ProductID=?", (id,))
        product = cursor.fetchone()
        
        print(product)
        
def get_all_product_info():
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        
        for product in products:
            print(product)          
   
   
def get_product_type_information(id):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from ProductType where ProductTypeID=?", (id,))
        product = cursor.fetchone()
        
        print(product)
        
def get_all_product_type_info():
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from ProductType")
        products = cursor.fetchall()
        
        for product in products:
            print(product)