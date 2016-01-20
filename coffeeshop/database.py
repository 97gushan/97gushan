import sqlite3

def create_table(db_name,table_name,sql):


    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True

        if(len(result) == 1):
            response = input("The table {0} already exist, do you wish to recreate it? (y/n): ".format(table_name))

            if(response == "y"):
                keep_table = False
                print("the {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False

        if(not keep_table):


            cursor.execute(sql)
            db.commit()


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
    create_product_table()
    create_product_type_table()
