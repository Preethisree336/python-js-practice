import mysql.connector
def connect_db():
     return mysql.connector.connect(  
        host="localhost",  
        user="root",    
        password="", 
        database="expense_db"
     )
def add_expense(title,amount,data):
    connn = connect_db
    cursor = conn.cursor() 
    query = "INSERT INTO expenses (title, amount, date) VALUES (%s, %s, %s)" 
    values = (title, amount, date)  
    cursor.execute(query, values)
    conn.commit() 
    conn.close()


def get_expenses(): 
    conn = connect_db() 
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM expenses") 
    data = cursor.fetchall() 
    conn.close()  
    return data

def get_total(): 
   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("SELECT SUM(amount) FROM expenses") 
   total = cursor.fetchone()[0]  
conn.close() 
return total if total else 0