from DB.conexion import Base
from sqlalchemy import Column, Integer, String

#Se procede a hacer el modelo de la tabla
class User(Base):
    __tablename__ = "tb_users"
    id = Column(Integer, primary_key=True, autoincrement = "auto" ,index=True) #Se declara la columna id como clave primaria
    name = Column(String) #Se declara la columna nombre como tipo string
    age = Column(Integer) #Se declara la columna edad como tipo entero
    email = Column(String) #Se declara la columna email como tipo string
   