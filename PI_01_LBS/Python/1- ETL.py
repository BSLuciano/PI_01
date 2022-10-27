
import pandas as pd
import os
import re 

# detalles en el notebook

# carga de archivos

path = r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\Datasets\precios_semanas_20200419_20200426.xlsx'
df_1 = pd.read_excel(path, sheet_name= None)

df_1_h1 = df_1['precios_20200426_20200426']
df_1_h2 = df_1['precios_20200419_20200419']

path_2 = r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\Datasets\precios_semana_20200413.csv' 
df_2 = pd.read_csv(path_2, encoding='utf-16-le', sep=',')

path_3 = r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\Datasets\precios_semana_20200503.json'
df_3 = pd.read_json(path_3)


path_5 = r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\Datasets\producto.parquet'
df_producto = pd.read_parquet(path_5, engine='pyarrow')

path_6 = r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\Datasets\sucursal.csv'
df_sucursal = pd.read_csv(path_6, sep=',')

# Eliminar duplicados

dicc = {'df_1_h1':df_1_h1, 'df_1_h2':df_1_h2, 'df_2':df_2,
         'df_3':df_3, 'df_sucursal':df_sucursal, 'df_producto':df_producto}

for key in dicc:
    dicc[key].drop_duplicates(inplace=True)

# Remplazar por 0 los valores faltantes

dicc = {'df_1_h1':df_1_h1, 'df_1_h2':df_1_h2, 'df_2':df_2,
         'df_3':df_3, 'df_sucursal':df_sucursal, 'df_producto':df_producto}
for key in dicc:
    for e in dicc[key]:
        dicc[key][e].fillna(0, inplace=True)

# Ordenar columnas

df_1_h1 = df_1_h1[['precio','producto_id','sucursal_id']]
df_1_h2 = df_1_h2[['precio','producto_id','sucursal_id']]

# Cambio de nombre de columna

df_producto = df_producto.rename(columns={'id':'producto_id'})

# Recucción de la cantidad de decimales de la columna precio

df_3.precio = df_3.precio.replace('',0) # Reemplazar str '' con 0, cambiar type 

df_2.precio = df_2.precio.astype(float);
df_1_h1.precio = df_1_h1.precio.astype(float);
df_1_h2.precio = df_1_h2.precio.astype(float);
df_3.precio = df_3.precio.astype(float);

df_1_h1.producto_id.fillna(0,inplace=True) # quitar registro nulos de df_1_h1.producto_id

df_2.precio = df_2.precio.round(2)
df_1_h1.precio = df_1_h1.precio.round(2)
df_1_h2.precio = df_1_h2.precio.round(2)
df_3.precio = df_3.precio.round(2)


# Corección sucursal_id

# Función para normalizar los id

df_1_h2.sucursal_id = df_1_h2.sucursal_id.astype(str)
df_2.sucursal_id = df_2.sucursal_id.astype(str)

def mod_id_suc (x):
    if ' 00:00:00' in x:
        x = x.replace(' 00:00:00','')
        val_1 = x.split('-')[0]
        val_2 = x.split('-')[1]
        val_3 = x.split('-')[2]
       
        x = val_3 + '-' + val_2 + '-' + val_1
    return x

df_2.sucursal_id = df_2.sucursal_id.apply(mod_id_suc)
df_1_h2.sucursal_id = df_1_h2.sucursal_id.apply(mod_id_suc)


# Crear columnas con las fechas de semana
        # Extracción de fechas de los nombres de los archivos
        
        # Extraer el texto del cual se sacará la fecha
df_2_texto = os.path.split(path_2)[1]
df_3_texto = os.path.split(path_3)[1]

lista = list(df_1.keys())
df_1_h1_texto = lista[0]
df_1_h2_texto = lista[1]

        # Extraer la fecha del texto
df_2_fecha = [int(df_2_semana) for df_2_semana in re.findall(r'\d+', df_2_texto)][0]
df_3_fecha = [int(df_3_semana) for df_3_semana in re.findall(r'\d+', df_3_texto)][0]
df_1_h1_fecha = [int(df_2_semana) for df_2_semana in re.findall(r'\d+', df_1_h1_texto)][0]
df_1_h2_fecha = [int(df_2_semana) for df_2_semana in re.findall(r'\d+', df_1_h2_texto)][0]

df_2['fecha_semana'] = df_2_fecha
df_3['fecha_semana'] = df_3_fecha
df_1_h1['fecha_semana'] = df_1_h1_fecha
df_1_h2['fecha_semana'] = df_1_h2_fecha


# Exportar DataFrames a csv

# ubicar csv en programdata para poder acceder a ellos desde mysql
df_1_h1.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\precios_semanas_20200426_20200426_mod_h1.csv', index=False)
df_1_h2.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\precios_semanas_20200419_20200419_mod_h2.csv', index=False)
df_2.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\precios_semana_20200413_mod.csv', index=False)
df_3.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\precios_semana_20200503_mod.csv', index=False)
df_producto.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\producto_mod.csv', index=False)
df_sucursal.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\PI-01\sucursal_mod.csv', index=False) 