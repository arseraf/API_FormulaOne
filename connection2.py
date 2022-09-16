import mysql.connector as sql


db= sql.connect (host = 'localhost',
            user = 'root',
            password = 'As$37040731',
            database = 'pi01'
        )
        
       
db  

cursor= db.cursor()
cursor.execute("SELECT * FROM constructors")

query = cursor.fetchall() 
print(query)