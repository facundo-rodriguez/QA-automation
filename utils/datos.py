import csv
import pathlib
import json

def leer_csv_login(ruta_archivo):
    
    ruta = pathlib.Path(ruta_archivo)
    datos = []
    
    with open(ruta,newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
    
            debe_funcionar = fila["debe_funcionar"].lower() == "true"

            datos.append((fila["usuario"], fila["password"], debe_funcionar))
    
    return datos



def leer_json_productos(ruta_archivo):
    
    ruta = pathlib.Path(ruta_archivo)

    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    nombres = [producto["nombre"] for producto in productos]
    return nombres