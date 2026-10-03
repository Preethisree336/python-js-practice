import mysql.connector
conn = mysql.connector.connect(
    host = "local host" ,
    user="root", 
    password="",
    database="expense_db"
     )
    
print("Connected successfully!")

