#Importo las librerías necesarias
from fastapi import FastAPI
import pandas as pd
from pandasql import sqldf
# creación de una aplicacion FastAPI
app = FastAPI()

#**************Carta de presentación**************
@app.get("/")
def presentacion():
    return "Proyecto Individual 01 - Carlos Alexis Farias Gallardo. Bienvenidos a mi API"

@app.get("/contacto")
def contacto():
    return "Email: cfarias.gallardo7@gmail.com / Github: CarlitosAlex"
# ***************QUERIS***************************
# Queri 1
# Esta función recibe como parámetros la plataforma requerida, el tipo de duración y el año de lanzamiento.
# Devuelve como resultado la PELICULA con mayor duración en el año indicado, disponible en esa plataforma.
Dataframe_streamings2 = pd.read_csv ("Dataframe_streamings2.csv")
DF_Rating2 =pd.read_csv ("DF_Rating.csv")
@app.get('/get_longest/{year}/{platform}/{duration_type}')
def get_max_duration(year, platform, duration_type):

    if platform == "amazon":
        inicial = "a%"
    elif platform == 'netflix':
        inicial = 'n%'
    elif platform == "hulu":
        inicial = "h%"
    elif platform == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'

    querie = f'select title, duration from Dataframe_streamings2 where id like "{inicial}" and type == "movie" and release_year == {year} order by duration_int desc limit 1'
    
    return sqldf (querie).to_string(index=False, header=False)
# Queri 2
# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
# Esta función recibe como parámetros la plataforma requerida, el puntaje y el año a buscar.
# Devuelve como resultado la cantidad de PELICULAS con puntaje mayor al indicado, que están disponibles en esa plataforma y se estrenaron en el año indicado.
Dataframe_streamings2 = pd.read_csv ("Dataframe_streamings2.csv")
DF_Rating2 =pd.read_csv ("DF_Rating.csv")

@app.get('/get_score_count/{platform}/{scored}/{year}')
def get_score_count(platform, scored, year):
    
    if platform == "amazon":
        inicial = "a%"
    elif platform == 'netflix':
        inicial = 'n%'
    elif platform == "hulu":
        inicial = "h%"
    elif platform == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'

    querie = f'select count(*) from DF_Rating2 where id like "{inicial}" and type == "movie" and score > {scored} and release_year == {year}'

    return platform, sqldf (querie).to_string(index=False, header=False)