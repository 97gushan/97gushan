import sqlite3

def delete_product(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where ProductID=?"
        cursor.execute(sql, data)
        db.commit()

def delete_product_type(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from ProductType where ProductTypeID=?"
        cursor.execute(sql, data)
        db.commit()
        
def delete_customer(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Customer where CustomerID=?"
        cursor.execute(sql, data)
        db.commit()
        
        print("Customer " + str(data[0]) + " removed")
        
if __name__ == "__main__":
    data = ("Latte",)
    delete_product(data)