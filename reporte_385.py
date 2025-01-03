import os
import json
import pandas as pd
from tqdm import tqdm
from unidecode import unidecode
from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, 'es_GT.UTF-8')

#########################LEER ARCHIVOS###########################
route = os.path.abspath('temporaly\consulta_385')
files =os.listdir(route)

##########################LEER DICT PARA CATEGORIZAR##########################
with open(os.path.abspath('dics\\bancosc.json'), 'r') as file:
    bancosc = json.load(file)

dfs = []
for file in tqdm(files):

    tables = pd.read_html(os.path.join(route, file))

    fecha = tables[0].iloc[2, 0].split()[-1]
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
    reservas = tables[0].iloc[3, 0].split()[-1]
    reservas = datetime.strptime(reservas, '%d/%m/%Y')

    df = tables[1]
    df = df.set_index(df.columns[0])
    df.columns = df.iloc[0,].tolist()
    df.index.name = 'BANCO' 
    df = df.iloc[1:,].stack().reset_index()
    df.columns = ['BANCO', 'CUENTA', 'VALOR']
    df['CUENTA'] = df['CUENTA'].str.replace(r'\b[bcd]/', '', regex=True).apply(lambda row: unidecode(row.strip().upper()))
    df['BANCO'] = df['BANCO'].apply(lambda row: unidecode(row.strip().upper()))

    df['FECHA'] = fecha
    df['RESERVA'] = reservas
    df['MONEDA'] = 'NACIONAL'
    df['DIMENSION'] = 'MILES DE QUETZALES'
    df['ORIGEN'] = 'ACTIVOS CREDITICIOS'

    dfs.append(df)

todo = pd.concat(dfs, axis=0).drop_duplicates()

print(todo)
todo.to_excel(os.path.join(os.path.abspath('outputs'),'reporte_385.xlsx'), index=False)