from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Creo la clase base para las tablas de la base de datos
Base = declarative_base()  # type: ignore

# Defino el modelo para la tabla 'leyendas'
class Leyenda(Base):  # type: ignore
    # Nombre de la tabla en la base de datos
    __tablename__ = "leyendas"

    # Defino los campos de la tabla
    id = Column(Integer, primary_key=True, index=True)  # id único para cada leyenda
    nombre = Column(String(255), nullable=False)  # El nombre de la leyenda, obligatorio
    categoria = Column(String(100))  # categoría de la leyenda
    descripcion = Column(Text)  # descripción más larga de la leyenda
    fecha = Column(Date)  # fecha asociada a la leyenda
    provincia = Column(String(100))  # provincia de la leyenda
    canton = Column(String(100))  # cantón de la leyenda
    distrito = Column(String(100))  # distrito de la leyenda
    imagen_url = Column(String(255))  # URL de la imagen asociada a la leyenda
    created_at = Column(TIMESTAMP, default=datetime.utcnow)  # creación automática de la leyenda
