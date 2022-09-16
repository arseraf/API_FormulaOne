

from fastapi import FastAPI

import json

from sqldb import database, first_query, second_query, third_query, fourth_query

# Implementación de FastAPI:

app = FastAPI(title= 'Formula 1 DataBase', version=1.0)



@app.get("/")
async def index():
    return "Bienvenido. Para realizar las siguientes consultas sobre la Fórmula 1, escriba el código indicado en la URL:                           /query1 : Año con más carreras.                                                                                                            /query2 : Piloto con mayor cantidad de primeros puestos.                                                                                                         /query3 : Nombre del circuito más corrido.                                                                                             /query4 : Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad americana o británica."
    
 

@app.get("/query1")
async def first():
    return first_query

@app.get("/query2")
async def second():
    return second_query

@app.get("/query3")
async def third():
    return third_query

@app.get("/query4")
async def fourth():
    return fourth_query    
    
