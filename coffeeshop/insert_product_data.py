import sqlite3

def insert_data(values):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql, values)
        db.commit()
        
 
if __name__ == "__main__":
    product = ("Black Tea", 3.14159265)
    insert_data(product)