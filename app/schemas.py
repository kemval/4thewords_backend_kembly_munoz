from pydantic import BaseModel
from datetime import date

# Base para los modelos de leyendas que se validarán
class LeyendaBase(BaseModel):
    nombre: str  # Nombre de la leyenda
    categoria: str  # Categoría de la leyenda
    descripcion: str  # Descripción completa de la leyenda
    fecha: date  # Fecha asociada a la leyenda
    provincia: str  # Provincia donde se encuentra la leyenda
    canton: str  # Cantón relacionado con la leyenda
    distrito: str  # Distrito relacionado con la leyenda
    imagen_url: str  # URL de la imagen asociada

# Modelo que se usa para la creación de leyendas, hereda de LeyendaBase
class LeyendaCreate(LeyendaBase):
    pass  # No añade nada nuevo, solo se usa para las validaciones al crear

# Modelo final de leyenda, incluye el campo 'id' para cuando ya existe en la base de datos
class Leyenda(LeyendaBase):
    id: int  # ID único de la leyenda en la base de datos

    # Configuración para que SQLAlchemy y Pydantic se entiendan bien
    class Config:
        from_attributes = True  # Permite que los objetos de SQLAlchemy sean compatibles con Pydantic
