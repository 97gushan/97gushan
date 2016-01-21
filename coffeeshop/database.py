import sqlite3

def create_table(db_name,table_name,sql):


    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME FROM SQLITE_MASTER WHERE NAME=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True

        if(len(result) == 1):
            response = input("The table {0} already exist, do you wish to recreate it? (y/n): ".format(table_name))

            if(response == "y"):
                keep_table = False
                print("the {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("DROP TABLE IF EXISTS {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False

        if(not keep_table):


            cursor.execute(sql)
            db.commit()

def create_customer_table(db_name):
    sql = """CREATE TABLE Customer
            (CustomerID INTEGER NOT NULL,
            FirstName TEXT,
            LastName TEXT,
            Street TEXT,
            Town TEXT,
            PostCode INTEGER,
            TelephoneNumber INTEGER,
            EMailAdress TEXT,
            PRIMARY KEY(CustomerID))"""
    create_table(db_name, "Customer", sql)
         
         
def create_customer_order_table():
    sql = """CREATE TABLE CustomerOrder
            (OrderID INTEGER NOT NULL,
            Date TEXT,
            Time TEXT,
            CustomerID INTEGER,
            FOREIGN KEY(CustomerID) references Customer(CustomerID),
            PRIMARY KEY(OrderID))"""
    create_table(db_name, "CustomerOrder", sql)
    
def create_order_item_table():
    sql = """ CREATE TABLE OrderItem(
            OrderItemID INTEGER NOT NULL,
            OrderID INTEGER,
            ProductID INTEGER,
            Quantity INTEGER,
            FOREIGN KEY(OrderID) references CustomerOrder(OrderID),
            FOREIGN KEY(ProductID) references Product(ProductID),
            PRIMARY KEY(OrderItemID))"""
    create_table(db_name, "OrderItem", sql)
    
def create_product_table():
    sql = """create table Product
             (ProductID INTEGER,
              name TEXT,
              Price REAL,
              ProductTypeID integer,
              foreign key(ProductID) references ProductType(ProductTypeID),
              primary key(ProductID))"""
    create_table(db_name, "Product",sql)


def create_product_type_table():
    sql = """create table ProductType
            (ProductTypeID integer,
            Description text,
            primary key(ProductTypeID))"""
    create_table(db_name, "ProductType", sql)

if __name__ == "__main__":
    db_name = "coffe_shop.db"
    create_customer_table()
    create_customer_order_table()
    create_order_item_table()
    create_product_table()
    create_product_type_table()
    
