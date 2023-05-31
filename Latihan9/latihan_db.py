import mysql.connector
 
# connecting to the mysql server
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_latihan9_dpbo"
)

# Insert
dbcursor = mydb.cursor()

sql = "INSERT INTO cust_address (name, address) VALUES (%s, %s)"
val = ("Ray", "Sesame Street 1206")
dbcursor.execute(sql, val)

mydb.commit()
print(dbcursor.rowcount, "record inserted")

sql = "INSERT INTO cust_address (name, address) VALUES (%s, %s)"
val = ("Cecil", "Land of Dawn")
dbcursor.execute(sql, val)

mydb.commit()
print(dbcursor.rowcount, "record inserted")

# Select
dbcursor = mydb.cursor()

dbcursor.execute("SELECT * FROM cust_address")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# Delete
dbcursor = mydb.cursor()

sql = "Delete FROM cust_address WHERE address = 'Highway 21'"
dbcursor.execute(sql)

mydb.commit()
print(dbcursor.rowcount, "record(s) deleted")
