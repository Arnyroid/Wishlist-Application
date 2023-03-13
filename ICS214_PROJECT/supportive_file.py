import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Arnyroid"
)

conn = mydb.cursor()
conn.execute("CREATE DATABASE IF NOT EXISTS ics214_project_wishlist;")
conn.execute("USE ics214_project_wishlist;")
conn.execute("CREATE TABLE IF NOT EXISTS login(un VARCHAR(100), pw VARCHAR(100))")
q = "INSERT into LOGIN(un,pw) VALUES('{}','{}');".format("admin","123456")
conn.execute(q)
mydb.commit()
conn.execute("CREATE TABLE IF NOT EXISTS amazon(id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(1000) NOT NULL, price varchar(200), url VARCHAR(2000));")
# conn.execute("ALTER TABLE amazon AUTO_INCREMENT = 1;")
conn.execute("CREATE TABLE IF NOT EXISTS flipkart(id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(1000) NOT NULL, price varchar(200), url VARCHAR(2000));")
# conn.execute("ALTER TABLE flipkart AUTO_INCREMENT = 1;")
mydb.commit()