import os
import json
import pandas as pd
from tqdm import tqdm
from unidecode import unidecode
from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, 'es_GT.UTF-8')

#########################LEER ARCHIVOS###########################
route = os.path.abspath('temporaly\consulta_383')
files =os.listdir(route)

##########################LEER DICT PARA CATEGORIZAR##########################
with open(os.path.abspath('dics\\bancosc.json'), 'r') as file:
    bancosc = json.load(file)

#########################LOOP DE ARCHIVOS###########################
dfs = []

for file in tqdm(files):
    tables = pd.read_html(os.path.join(route, file))

    fecha = tables[0].iloc[2,0].replace('Información referida al ', '')
    fecha = datetime.strptime(fecha, '%d de %B de %Y').replace(day=1)

    df = tables[1]
    df = df.set_index(df.columns[0])
    df.columns = df.iloc[0,].tolist()
    df.index.name = 'CUENTA' 
    df = df.iloc[1:,].stack().reset_index()
    df['CUENTA'] = df['CUENTA'].apply(lambda row: unidecode(row.strip().upper()))
    df[df.columns[1]] = df[df.columns[1]].apply(lambda row: unidecode(row.strip().upper()))
    df['FECHA'] = fecha
    df['MONEDA'] = 'AMBAS'
    df['ORIGEN'] = 'PERFIL FINANCIERO'
    df['DIMENSION'] = 'QUETZALES'

    dfs.append(df)

todo = pd.concat(dfs, axis=0).drop_duplicates()
todo.columns = ['CUENTA', 'BANCO', 'VALOR', 'FECHA', 'MONEDA', 'ORIGEN', 'DIMENSION']
todo['BANCO'] =todo['BANCO'].map(bancosc)
print(todo)

todo.to_excel(os.path.join(os.path.abspath('outputs'),'reporte_383.xlsx'), index=False)