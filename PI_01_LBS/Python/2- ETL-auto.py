import pandas as pd
import os
import re
from ruta import *

def carga(path):
    df_precio = pd.read_csv(f'{path}',  sep= '|')
    df_precio.drop_duplicates(inplace=True)
    df_precio.fillna(0, inplace=True)
    df_precio = df_precio[['Precio','IdProducto','IdSucursal']]
    df_precio.Precio = df_precio.Precio.replace('',0)
    df_precio.Precio = df_precio.Precio.astype(float)
    df_precio.Precio = df_precio.Precio.round(2)

    #df_precio = df_precio.rename(columns={'precio':'Precio','producto_id':'IdProducto','sucursal_id':'IdSucursal'})
    
    df_precio.IdSucursal = df_precio.IdSucursal.astype(str)
    def mod_id_suc (x):
        if ' 00:00:00' in x:
            x = x.replace(' 00:00:00','')
            val_1 = x.split('-')[0]
            val_2 = x.split('-')[1]
            val_3 = x.split('-')[2]
            
            x = val_3 + '-' + val_2 + '-' + val_1
        return x

    df_precio.IdSucursal = df_precio.IdSucursal.apply(mod_id_suc)

    df_precio_texto = os.path.split(path)[1]
    df_precio_fecha = [int(df_precio_semana) for df_precio_semana in re.findall(r'\d+', df_precio_texto)][0]
    df_precio['fecha_semana'] = df_precio_fecha

    df_precio.to_sql('precio', coneccion, if_exists='append', index=False)


    
    
  

carga(r'C:\Users\barce\OneDrive\Escritorio\HENRY\HENRY_Course\1- Data_Science\Proyectos\1- Individual\PI - 1\PI01_DATA_ENGINEERING-main\PI_01\Datasets\precios_semana_20200518.txt')
