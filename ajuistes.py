import os
import json
import pandas as pd
from tqdm import tqdm

##################################################################
def cargar_diccionario(nombre_archivo):
    with open(os.path.abspath(f'dics/{nombre_archivo}.json'), 'r') as file:
        data = json.load(file)
    return {key: value["ID"] for key, value in data.items()}

##################################################################
diccionarios = {
    'bancos': cargar_diccionario('Bancos'),
    'origen': cargar_diccionario('Origen'),
    'tia': cargar_diccionario('Tia'),
    'moneda': cargar_diccionario('Moneda'),
    'dimension': cargar_diccionario('Dimension'),
    'contable': cargar_diccionario('Contable'),
    'region': cargar_diccionario('Region'),
    'integracion': cargar_diccionario('Integracion'),
    'fideicomiso': cargar_diccionario('Fideicomiso'),
    'vencida': cargar_diccionario('Vencida'),
    'agrupacion': cargar_diccionario('Agrupacion'),
    'clasificacion': cargar_diccionario('Clasificacion'),
    'tipo': cargar_diccionario('Tipo'),
    'evolucion': cargar_diccionario('Evolucion'),
    'perfil': cargar_diccionario('Perfil'), 
    'activos': cargar_diccionario('Activos')
    
}

# Función para procesar un DataFrame
def procesar_reporte(ruta_archivo, columnas_map):
    df = pd.read_excel(os.path.abspath(ruta_archivo))
    for columna, diccionario in columnas_map.items():
        df[columna] = df[columna].map(diccionarios[diccionario])
    return df

# Definición de los reportes y las columnas a mapear
reportes = {
    'outputs/reporte_18me.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'tia', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_18mn.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'tia', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_23me.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'contable', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_23mn.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'contable', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_24.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'integracion', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_25.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'vencida', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_26me.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'agrupacion', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_26mn.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'agrupacion', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_37.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'CUENTA': 'fideicomiso', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_43.xlsx': {'BANCO': 'bancos', 'ORIGEN': 'origen', 'REGION': 'region'},
    'outputs/reporte_248me.xlsx': {'TIPO': 'tipo', 'CUENTA': 'evolucion', 'CLASIFICACION': 'clasificacion', 'MONEDA': 'moneda'},
    'outputs/reporte_248mn.xlsx': {'TIPO': 'tipo', 'CUENTA': 'evolucion', 'CLASIFICACION': 'clasificacion', 'MONEDA': 'moneda'},
    'outputs/reporte_383.xlsx': {'BANCO': 'bancos', 'CUENTA': 'perfil', 'ORIGEN': 'origen', 'MONEDA': 'moneda', 'DIMENSION':'dimension'},
    'outputs/reporte_385.xlsx': {'BANCO': 'bancos', 'CUENTA': 'activos', 'ORIGEN': 'origen', 'MONEDA': 'moneda', 'DIMENSION':'dimension'}

}

# Procesar y mostrar cada reporte

dfs = []
for ruta, columnas_map in tqdm(reportes.items()):
    df = procesar_reporte(ruta, columnas_map)
    
    if ruta not in ['outputs/reporte_43.xlsx', 'outputs/reporte_248me.xlsx', 'outputs/reporte_248mn.xlsx']:
        dfs.append(df)


todo = pd.concat(dfs, axis=0)
todo.to_excel(os.path.join(os.path.abspath('outputs'), 'sib1.xlsx'), index=False)
todo = todo.fillna(0)
print(todo)

    
