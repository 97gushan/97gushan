import sqlite3

def query(sql,data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit()

def insert_product_type_data(records):
    sql = "insert into ProductType(Description) values (?)"

    for record in records:
        query(sql, record)

def insert_product_data(records):
    sql = "insert into Product (Name, Price, ProductTypeID) values (?,?,?)"

    for record in records:
        query(sql, record)
        
def insert_customer_data(record):
    sql = "INSERT INTO Customer (FirstName, LastName, Street, Town, PostCode, TelephoneNumber, EMailAdress) values (?,?,?,?,?,?,?)"
    query(sql, record)


if __name__ == "__main__":
    product_types = [("Coffe",),("Tea",),("Cold Drink",)]
    #insert_product_type_data(product_types)

    products = [("Americano", 2.0, 6),("Mocha", 3.5, 7), ("Green Tea", 1.25, 8)]
    insert_product_data(products)
