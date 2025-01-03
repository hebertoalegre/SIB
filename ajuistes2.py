import os
import json
import pandas as pd
from tqdm import tqdm

##################################################################
def cargar_diccionario(nombre_archivo):
    with open(os.path.abspath(f'dics/{nombre_archivo}.json'), 'r') as file:
        data = json.load(file)
    return {key: value["ID"] for key, value in data.items()}

diccionarios = {
    'region': cargar_diccionario('Region'),
    'bancos': cargar_diccionario('Bancos'),
    'origen': cargar_diccionario('Origen'),
    'moneda': cargar_diccionario('Moneda'),
    'dimension': cargar_diccionario('Dimension'),
    'tipo': cargar_diccionario('Tipo'),
    'evolucion': cargar_diccionario('Evolucion'),
    'clasificacion': cargar_diccionario('Clasificacion')

    
}


# Función para procesar un DataFrame
def procesar_reporte(ruta_archivo, columnas_map):
    df = pd.read_excel(os.path.abspath(ruta_archivo))
    for columna, diccionario in columnas_map.items():
        df[columna] = df[columna].map(diccionarios[diccionario])
    return df


# Definición de los reportes y las columnas a mapear
reportes = {
    'outputs/reporte_43.xlsx': {'BANCO': 'bancos', 'REGION': 'region', 'ORIGEN': 'origen', 'DIMENSION':'dimension'},
    'outputs/reporte_248mn.xlsx': {'TIPO': 'tipo', 'CUENTA': 'evolucion', 'CLASIFICACION': 'clasificacion', 'MONEDA': 'moneda', 'ORIGEN':'origen','DIMENSION':'dimension'},
    'outputs/reporte_248me.xlsx': {'TIPO': 'tipo', 'CUENTA': 'evolucion', 'CLASIFICACION': 'clasificacion', 'MONEDA': 'moneda', 'ORIGEN':'origen', 'DIMENSION':'dimension'}
}

sf = []
agencias = []
for ruta, columnas_map in tqdm(reportes.items()):
    df = procesar_reporte(ruta, columnas_map)
    if ruta not in ['outputs/reporte_43.xlsx']:
        sf.append(df)
    else:
        agencias.append(df)


todo = pd.concat(sf, axis=0)
todo.to_excel(os.path.join(os.path.abspath('outputs'), 'sf.xlsx'), index=False)
print(todo)

todo = pd.concat(agencias, axis=0)
todo.to_excel(os.path.join(os.path.abspath('outputs'), 'agencias.xlsx'), index=False)
print(todo)

    