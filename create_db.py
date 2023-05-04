import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(category_ID INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS sales(sid INTEGER PRIMARY KEY AUTOINCREMENT,invoice text,product_ID text,Product_Name text,Product_Price text,Quantity text,cname text,cphone text,netprice text,date text)")
    con.commit() 

create_db()    


