import mysql.connector
import pandas as pd
import os
from tqdm import tqdm


def load_excel_sheet(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['VALOR'] = df['VALOR'].apply(lambda row: float(row) if row != '_' else 0 )
    return df

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='bantrab',
        database='sib_data'
    )

def insert_data(table_name, columns, data, update_columns):
    """
    Inserta datos en una tabla MySQL con manejo de duplicados.

    Args:
        table_name (str): Nombre de la tabla.
        columns (list): Lista de nombres de columnas.
        data (iterable): Datos a insertar.
        update_columns (list): Columnas a actualizar en caso de duplicados.
    """
    placeholders = ", ".join(["%s"] * len(columns))
    update_placeholders = ", ".join([f"{col}=VALUES({col})" for col in update_columns])

    query = f"""
    INSERT INTO {table_name} ({', '.join(columns)})
    VALUES ({placeholders})
    ON DUPLICATE KEY UPDATE {update_placeholders};
    """

    con = connect_to_database()
    cursor = con.cursor()

    for row in tqdm(data):
        cursor.execute(query, row)
    
    con.commit()
    cursor.close()
    con.close()

def process_sheets_to_table(sheet_config, file_path):
    """
    Procesa múltiples hojas de Excel y las inserta en tablas de MySQL.

    Args:
        sheet_config (list): Lista de configuraciones con el formato:
            [{"sheet_name": str, "table_name": str, "columns": list, "update_columns": list}]
        file_path (str): Ruta del archivo Excel.
    """
    for config in sheet_config:
        print(f"Procesando hoja: {config['sheet_name']} para la tabla: {config['table_name']}")
        df = load_excel_sheet(file_path, config['sheet_name'])
        data = df[config['columns']].values.tolist()
        insert_data(config['table_name'], config['columns'], data, config['update_columns'])

# Ruta del archivo principal y diccionarios
main_file = os.path.abspath('outputs/sf.xlsx')
main_file1 = os.path.abspath('outputs/agencias.xlsx')


# Configuración para las tablas y hojas
sheet_config = [
    {"sheet_name": "Sheet1", "table_name": "sistema_financiero", 
     "columns": ["TIPO", "FECHA", "CUENTA", "VALOR", "CLASIFICACION", "MONEDA", "ORIGEN", "DIMENSION"], 
     "update_columns": ["TIPO", "FECHA", "CUENTA", "VALOR", "CLASIFICACION", "MONEDA", "ORIGEN", "DIMENSION"]}

]


process_sheets_to_table(sheet_config, main_file)



sheet_config = [
     {"sheet_name": "Sheet1", "table_name": "agencias", 
     "columns": ["BANCO", "REGION", "VALOR", "FECHA", "ORIGEN", "DIMENSION"], 
     "update_columns": ["BANCO", "REGION", "VALOR", "FECHA", "ORIGEN", "DIMENSION"]},

]

process_sheets_to_table(sheet_config, main_file1)
