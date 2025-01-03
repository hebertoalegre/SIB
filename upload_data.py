import mysql.connector
import pandas as pd
import os
from tqdm import tqdm


# def load_excel_sheet(file_path, sheet_name):
#     df = pd.read_excel(file_path, sheet_name=sheet_name)
#     df['DIMENSION'] = df.apply(lambda row: row['DIMENSION'] if "%" not in str(row['VALOR']) else 2, axis=1) 
#     df['VALOR'] = df['VALOR'].apply(lambda row: float(str(row).replace(',','')) if "%" not in str(row) else float(str(row).replace(',','').replace('%','')))
#     return df

def load_excel_sheet(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
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

# # Ruta del archivo principal y diccionarios
# dics_file = os.path.abspath('dics/dic_all.xlsx')

# # Configuración para las tablas y hojas
# sheet_config = [
#     {"sheet_name": "BANCOS", "table_name": "bancos", "columns": ["ID", "ABRE", "BANCO"], "update_columns": ["ABRE", "BANCO"]},
#     {"sheet_name": "ORIGEN", "table_name": "origen", "columns": ["ID", "ORIGEN"], "update_columns": ["ORIGEN"]},
#     {"sheet_name": "MONEDA", "table_name": "moneda", "columns": ["ID", "MONEDA"], "update_columns": ["MONEDA"]},
#     {"sheet_name": "DIMENSION", "table_name": "dimension", "columns": ["ID", "DIMENSION"], "update_columns": ["DIMENSION"]},
#     {"sheet_name": "REGION", "table_name": "region", "columns": ["ID", "REGION"], "update_columns": ["REGION"]},
#     {"sheet_name": "PERFIL", "table_name": "perfil", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "CLASIFICACION_CARTERA", "table_name": "clasificacion", "columns": ["ID", "CLASIFICACION", "ORIGEN"], "update_columns": ["CLASIFICACION", "ORIGEN"]},
#     {"sheet_name": "TIPO_CARTERA", "table_name": "tipo", "columns": ["ID", "TIPO", "ORIGEN"], "update_columns": ["TIPO", "ORIGEN"]},
#     {"sheet_name": "TIA", "table_name": "tia", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "CLASIFICACION_CONTABLE", "table_name": "contable", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "INTEGRACION", "table_name": "integracion", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "VENCIDA", "table_name": "vencida", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "FIDEICOMISO", "table_name": "fideicomiso", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "EVOLUCION", "table_name": "evolucion", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "CREDITOS_AGRUPACION", "table_name": "agrupacion", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]},
#     {"sheet_name": "ACTIVOS_CREDITICIOS", "table_name": "activos_crediticios", "columns": ["ID", "CUENTA", "ORIGEN"], "update_columns": ["CUENTA", "ORIGEN"]}
# ]


# process_sheets_to_table(sheet_config, dics_file)



# Ruta del archivo principal y diccionarios
main_file = os.path.abspath('outputs/sib1.xlsx')

# Configuración para las tablas y hojas
sheet_config = [
    {"sheet_name": "Sheet1", 
     "table_name": "sib", "columns": ["BANCO", "CUENTA", "VALOR", "FECHA", "MONEDA", "ORIGEN", "DIMENSION"], 
     "update_columns": ["BANCO", "CUENTA", "VALOR", "FECHA", "MONEDA", "ORIGEN", "DIMENSION"]},
]


process_sheets_to_table(sheet_config, main_file)


# # Ruta del archivo principal y diccionarios
# dics_file = os.path.abspath('outputs\departamentos.xlsx')



# # Configuración para las tablas y hojas
# sheet_config = [
#     {"sheet_name": "Sheet1", 
#      "table_name": "departamentos", "columns": ["GEOMETRY", "KEY_DEPTO", "DEPARTAMENTO","CENTROIDE_LAT", "CENTROIDE_LON", "KEY_EVOL"], 
#      "update_columns": ["GEOMETRY", "KEY_DEPTO", "DEPARTAMENTO","CENTROIDE_LAT", "CENTROIDE_LON", "KEY_EVOL"]},
# ]

# process_sheets_to_table(sheet_config, dics_file)