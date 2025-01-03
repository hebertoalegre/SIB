import pandas as pd
import os
import json

###########################################
# # Leer el archivo .xlsx
# df = pd.read_excel(os.path.abspath('dics\dic_243.xlsx'))

# # Convertir el DataFrame en un diccionario donde la primera columna es la clave y la segunda es el valor
# resultado = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

# # Guardar como archivo .json

# with open(os.path.abspath('dics\dic_243.json'), 'w') as json_file:
#     json.dump(resultado, json_file, indent=4, ensure_ascii=False)



###########################################
# BANCOS
bancos = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='BANCOS', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Bancos.json'), 'w') as json_file:
    json.dump(bancos, json_file, indent=4, ensure_ascii=False)


###########################################
# ORIGEN
origen = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='ORIGEN', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Origen.json'), 'w') as json_file:
    json.dump(origen, json_file, indent=4, ensure_ascii=False)

###########################################
# PERFIL
perfil = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='PERFIL', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Perfil.json'), 'w') as json_file:
    json.dump(perfil, json_file, indent=4, ensure_ascii=False)


###########################################
# MONEDA
moneda = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='MONEDA', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Moneda.json'), 'w') as json_file:
    json.dump(moneda, json_file, indent=4, ensure_ascii=False)

###########################################
# DIMENION
dimension = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='DIMENSION', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Dimension.json'), 'w') as json_file:
    json.dump(dimension, json_file, indent=4, ensure_ascii=False)

###########################################
# REGION
region = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='REGION', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Region.json'), 'w') as json_file:
    json.dump(region, json_file, indent=4, ensure_ascii=False)


###########################################
# CLASIFICACION_CARTERA
clasificacion = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='CLASIFICACION_CARTERA', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Clasificacion.json'), 'w') as json_file:
    json.dump(clasificacion, json_file, indent=4, ensure_ascii=False)

###########################################
# TIPO CARTERA
tipo = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='TIPO_CARTERA', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Tipo.json'), 'w') as json_file:
    json.dump(tipo, json_file, indent=4, ensure_ascii=False)


###########################################
# TASAS DE INTERES ACTIVAS
tia = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='TIA', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Tia.json'), 'w') as json_file:
    json.dump(tia, json_file, indent=4, ensure_ascii=False)

###########################################
# CLASIFICACION CONTABLE
contable = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='CLASIFICACION_CONTABLE', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Contable.json'), 'w') as json_file:
    json.dump(contable, json_file, indent=4, ensure_ascii=False)

###########################################
# INTEGRACION
integracion = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='INTEGRACION', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Integracion.json'), 'w') as json_file:
    json.dump(integracion, json_file, indent=4, ensure_ascii=False)

###########################################
# CREDITOS_AGRUPACION
agrupacion = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='CREDITOS_AGRUPACION', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Agrupacion.json'), 'w') as json_file:
    json.dump(agrupacion, json_file, indent=4, ensure_ascii=False)

###########################################
# FIDEICOMISO
fideicomiso = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='FIDEICOMISO', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Fideicomiso.json'), 'w') as json_file:
    json.dump(fideicomiso, json_file, indent=4, ensure_ascii=False)

###########################################
# VENCIDA
vencida = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='VENCIDA', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Vencida.json'), 'w') as json_file:
    json.dump(vencida, json_file, indent=4, ensure_ascii=False)

###########################################
# EVOLUCION
evolucion = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='EVOLUCION', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Evolucion.json'), 'w') as json_file:
    json.dump(evolucion, json_file, indent=4, ensure_ascii=False)

###########################################
# ACTIVOS_CREDITICIOS
activos = pd.read_excel(os.path.abspath('dics\dic_all.xlsx'), sheet_name='ACTIVOS_CREDITICIOS', index_col=0).to_dict('index')
with open(os.path.abspath('dics\Activos.json'), 'w') as json_file:
    json.dump(activos, json_file, indent=4, ensure_ascii=False)