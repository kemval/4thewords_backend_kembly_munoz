from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargo las variables de entorno desde el archivo .env
load_dotenv()

# Obtengo la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Si no está definida la URL de la base de datos, lanzo un error
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

# Creo el motor de la base de datos usando la URL que obtuve
engine = create_engine(DATABASE_URL)

# Creo una fábrica de sesiones, que usaré para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Inicializo los metadatos que usaré para las tablas
metadata = MetaData()
