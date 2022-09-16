import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Se crean los dataframes:

driver = pd.read_csv('Datasets\drivers.csv', sep=';')

circuits = pd.read_csv('Datasets\circuits.csv', sep=',')

constructors = pd.read_csv('Datasets\constructors.csv', sep=';')

pit_stops = pd.read_csv('Datasets\pit_stops.csv', sep=';')

races = pd.read_csv('Datasets/races.csv', sep=',')

results = pd.read_csv('Datasets/results.csv', sep=';')

# Se establece una conexion con MySQL:

sqlEngine = create_engine ("mysql+pymsql://root:As$37040731@localhost:3306/")

dbConnection = sqlEngine.connect()

try:
    frame = driver.to_sql(dbConnection, if_exists='fail');

except ValueError as vx:

    print(vx)

except Exception as ex:   

    print(ex)

else:

    print("Table created successfully.");   

finally:

    dbConnection.close()