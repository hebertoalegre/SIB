import mysql.connector
from mysql.connector import Error


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "bantrab",
}

db_name = "sib_data"

# Definiciones de tablas
table_definitions = {
    "sib": """
        CREATE TABLE IF NOT EXISTS sib (
            id INT AUTO_INCREMENT PRIMARY KEY,
            BANCO INT,
            CUENTA INT,
            VALOR DECIMAL(18, 3),
            FECHA DATE,
            MONEDA INT,
            ORIGEN INT, 
            DIMENSION INT
        )
    """,
    "bancos": """
        CREATE TABLE IF NOT EXISTS bancos (
            ID INT PRIMARY KEY,
            BANCO VARCHAR(255),
            ABRE VARCHAR(255)
        )
    """,
    "origen": """
        CREATE TABLE IF NOT EXISTS origen (
            ID INT PRIMARY KEY,
            ORIGEN VARCHAR(255)
        )
    """,
    "moneda": """
        CREATE TABLE IF NOT EXISTS moneda (
            ID INT PRIMARY KEY,
            MONEDA VARCHAR(255)
        )
    """,
    "dimension": """
        CREATE TABLE IF NOT EXISTS dimension (
            ID INT PRIMARY KEY,
            DIMENSION VARCHAR(255)
        )
    """,
    "region": """
        CREATE TABLE IF NOT EXISTS region (
            ID INT PRIMARY KEY,
            REGION VARCHAR(255)
        )
    """,
    "perfil": """
        CREATE TABLE IF NOT EXISTS perfil (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "clasificacion": """
        CREATE TABLE IF NOT EXISTS clasificacion (
            ID INT PRIMARY KEY,
            CLASIFICACION VARCHAR(255),
            ORIGEN INT
        )
    """,
    "tipo": """
        CREATE TABLE IF NOT EXISTS tipo (
            ID INT PRIMARY KEY,
            TIPO VARCHAR(255),
            ORIGEN INT
        )
    """,
    "tia": """
        CREATE TABLE IF NOT EXISTS tia (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "contable": """
        CREATE TABLE IF NOT EXISTS contable (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "integracion": """
        CREATE TABLE IF NOT EXISTS integracion (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "vencida": """
        CREATE TABLE IF NOT EXISTS vencida (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "fideicomiso": """
        CREATE TABLE IF NOT EXISTS fideicomiso (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "agrupacion": """
        CREATE TABLE IF NOT EXISTS agrupacion (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,
    "evolucion": """
        CREATE TABLE IF NOT EXISTS evolucion (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """,

    "sistema_financiero": """
        CREATE TABLE IF NOT EXISTS sistema_financiero (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            TIPO INT,
            FECHA DATE,
            CUENTA INT,
            VALOR DECIMAL(18, 3),
            CLASIFICACION INT,
            MONEDA INT,
            ORIGEN INT, 
            DIMENSION INT
            
        )
    """,
    "agencias": """
        CREATE TABLE IF NOT EXISTS agencias (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            BANCO INT,
            REGION INT,
            VALOR DECIMAL(18, 3),
            FECHA DATE,
            ORIGEN INT, 
            DIMENSION INT
            
        )
    """,
    "departamentos":"""
        CREATE TABLE IF NOT EXISTS departamentos(
            ID INT AUTO_INCREMENT PRIMARY KEY, 
            DEPARTAMENTO VARCHAR(255),
            CENTROIDE_LAT DECIMAL(10, 7),
            CENTROIDE_LON DECIMAL(10, 7), 
            GEOMETRY TEXT, 
            KEY_DEPTO INT, 
            KEY_EVOL INT
        )
    """,
      "activos_crediticios": """
        CREATE TABLE IF NOT EXISTS activos_crediticios (
            ID INT PRIMARY KEY,
            CUENTA VARCHAR(255),
            ORIGEN INT
        )
    """

    

}

try:
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.database = db_name
        
        # Crear tablas
        for table_name, table_query in table_definitions.items():
            cursor.execute(table_query)
            print(f"Tabla '{table_name}' creada o ya existe.")

        print("Todas las tablas se han creado exitosamente.")

except Error as e:
    print(f"Error: {e}")
