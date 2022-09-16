import pymysql as sql

class Database:
    def __init__(self):
        self.connection = sql.connect(              # Conexión con MySQL
            host = 'localhost',
            user = 'root',
            password = 'As$37040731',
            db = 'pi01',
            port = 3306, 
            
        )
        
        self.cursor = self.connection.cursor()
        print ("Connection Established")
    
    def Year_with_more_races (self):
        query1 = "SELECT YEAR(date), count(*) as Num_Carreras FROM races GROUP BY YEAR (date) ORDER BY Num_Carreras DESC" 
        self.cursor.execute(query1)
        query1_r = self.cursor.fetchone()
        year = query1_r[0]
        num_races = query1_r[1]
        return ("El año con más carreras fue " + str(year) + " (" + str(num_races) + " carreras).") 
        
        
    def top_GP_winner (self):
        query2= "SELECT d.forename as Nombre, d.surname as Apellido,  count(r.positionOrder) as Victorias FROM results r JOIN drivers d ON r.driverId = d.driverId WHERE r.positionOrder = 1 GROUP BY d.driverId ORDER BY count(r.positionOrder) DESC"
        self.cursor.execute(query2)
        query2_r = self.cursor.fetchone()
        driver_forename= query2_r[0]
        driver_surname= query2_r[1]
        victories = query2_r[2]
        return ("El piloto con más primeros puestos es " + (str(driver_forename)) + " " + (str(driver_surname)) + " (" + str(victories) + " victorias).") 
            
        
    def top_circuit(self):
        query3 = "SELECT name as Circuit, count(*) as Num_GrandPrixs FROM races GROUP BY circuitId ORDER BY count(*) DESC"
        self.cursor.execute(query3)
        query3_r = self.cursor.fetchone()
        circuit = query3_r[0]
        numgp = query3_r[1]
        return ("El circuito con más carreras corridas es el " + (str(circuit)) + " (Autodromo Nazionale di Monza) con " + str(numgp) + " grandes premios.") 
        
        
    def  most_points (self):
        query4 = "SELECT d.forename as Nombre, d.surname as Apellido, SUM(res.points) as Total_Points, c.nationality as Constructor_Nat FROM results res JOIN drivers d ON res.driverId = d.driverId JOIN constructors c ON res.constructorId = c.constructorId WHERE (c.nationality = 'British' OR c.nationality = 'American') GROUP BY d.driverId ORDER BY SUM(res.points) DESC"
        self.cursor.execute(query4)
        query4_r = self.cursor.fetchone()
        driver_forename= query4_r[0]
        driver_surname= query4_r[1]
        t_points = query4_r[2]
        return ("El piloto que consiguió más puntos corriendo para un constructor británico o americano es " + (str(driver_forename)) + " " + (str(driver_surname)) + " (" + str(t_points) + " puntos).") 
               
            
database = Database()
database


first_query = database.Year_with_more_races()
second_query = database.top_GP_winner()
third_query = database.top_circuit()
fourth_query = database.most_points()