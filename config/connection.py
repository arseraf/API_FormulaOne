import pymysql as sql

class Database:
    def __init__(self):
        self.connection = sql.connect(
            host = 'localhost',
            user = 'root',
            password = 'As$37040731',
            db = 'pi01'
        )
        
        self.cursor = self.connection.cursor()
        print ("Connection Established")
    
    def Year_with_more_races (self):
        query1 = "SELECT YEAR(date), count(*) as Num_Carreras FROM races GROUP BY YEAR (date) ORDER BY Num_Carreras DESC" 
        try:
            self.cursor.execute(query1)
            query1_r = self.cursor.fetchone()
            year = query1_r[0]
            num_races = query1_r[1]
            print ("El año con más carreras fue " + str(year) + " (" + str(num_races) + " carreras)") 
        except Exception as e:
            raise
        
    #def top_GP_winner (self):
    #    query1= ""
            
database = Database()
database.Year_with_more_races()