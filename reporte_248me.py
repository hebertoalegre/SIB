import os
import pandas as pd
from tqdm import tqdm
from unidecode import unidecode
from datetime import datetime
import json


##########################LEER DICT PARA CATEGORIZAR##########################
with open(os.path.abspath('dics\dic_243.json'), 'r') as file:
    python_obj = json.load(file)

#########################LEER ARCHIVOS###########################
route = os.path.abspath('temporaly\consulta_248me')
files =os.listdir(route)


#########################LOOP DE ARCHIVOS###########################
dfs = []
for file in tqdm(files):

    tables = pd.read_html(os.path.join(route, file), index_col=0)

    df = tables[2].T.reset_index()
    df[df.columns[0]] = df[df.columns[0]].apply(lambda row: row.split('.')[0] if '.' in row else row)
    idx = ['Área Geográfica', 'Destino del activo crediticio', 'Garantía', 'Plazo Otorgado', 'Monto Concedido']
    df = df[(df['index'].isin(['NÚMERO DE CRÉDITOS', 'SALDOS Quetzales', 'PARTICIPACIÓN (%)', 'MOROSIDAD (%)', 'TASA DE INTERÉS (%)']))]
    df = df.drop(idx, axis=1).set_index([df.columns[0], df.columns[1]]).stack().reset_index()
    
    dfs.append(df)

todo = pd.concat(dfs, axis=0)
todo[todo.columns[0]] = todo[todo.columns[0]].apply(lambda row: unidecode(row.strip()))
todo[todo.columns[2]] = todo[todo.columns[2]].apply(lambda row: unidecode(row.replace('_','').strip()))
todo['CATEGORIA'] = todo[todo.columns[2]].map(python_obj)
todo['MONEDA'] = 'EXTRANJERA'
todo['ORIGEN'] = 'EVOLUCION DE LA CARTERA DE CREDITOS'
todo['DIMENSION'] = 'QUETZALES'
todo.columns = ['TIPO', 'FECHA', 'CUENTA', 'VALOR','CLASIFICACION', 'MONEDA', 'ORIGEN', 'DIMENSION']
todo['VALOR'] = todo['VALOR'].astype(str).replace('_',0).astype(float)

todo['FECHA'] = todo['FECHA'].apply(lambda row: datetime.strptime(row, '%d/%m/%Y').replace(day=1))


todo = todo.sort_values(by=['VALOR'], ascending= True)
todo = todo.drop_duplicates( subset=['TIPO', 'FECHA', 'CUENTA', 'CLASIFICACION', 'MONEDA', 'ORIGEN', 'DIMENSION'], keep='last')

print(todo)
todo.to_excel(os.path.join(os.path.abspath('outputs'),'reporte_248me.xlsx'), index=False)