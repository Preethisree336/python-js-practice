# import mysql.connector
# mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="work_db"


# )
# print("database connected succesfully")

import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student info"


)
cursor = db.cursor()

# sql = "INSERT INTO student (name,age,course) VALUES (%s,%s,%s)"
# values = ("Ravi",20,"Developer")

cursor.execute("SELECT * FROM student")
rows = cursor.fetchone()
# for row in rows:
# print(row)
db.close()    
# print("Database connected successfully")