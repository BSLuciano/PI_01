import pandas as pd
import sqlalchemy as db

database_username='root' # Nomre de cliente en MySQL Workbrench
database_password='root' # Contraseña de MySQL Workbrench
database_ip='localhost'
database_name='MERCADO' # Nombre de Base de datos a donde nos conectaremos
database_conection=db.create_engine(f'mysql+pymysql://{database_username}:{database_password}@{database_ip}/{database_name}')
coneccion=database_conection.connect()
metadata=db.MetaData()