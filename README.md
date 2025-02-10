
# 4thewords Backend - Kembly Muñoz

Este es el proyecto backend para el libro virtual de leyendas costarricenses, desarrollado con **FastAPI**, **SQLAlchemy** y **MySQL**. La API permite manejar leyendas costarricenses con filtros, creación, actualización y eliminación.

## Requisitos

- Python 3.9 o superior
- MySQL 8.0 o superior
- Dependencias listadas en `requirements.txt`
- **Git** (si deseas clonar el proyecto desde GitHub)

## Instalación y Configuración

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/4thewords_backend_kembly_munoz.git
cd 4thewords_backend_kembly_munoz
```

### 2. Crear un entorno virtual

Es recomendable crear un entorno virtual para gestionar las dependencias de manera aislada. Si no tienes un entorno virtual, crea uno usando el siguiente comando:

```bash
python3 -m venv venv
```

Luego, activa el entorno virtual:

- **En Windows**:

```bash
venv\Scripts\activate
```

- **En macOS/Linux**:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

Con el entorno virtual activo, instala las dependencias del proyecto usando el siguiente comando:

```bash
pip install -r requirements.txt
```

Esto instalará todas las librerías necesarias como FastAPI, SQLAlchemy, MySQL y otras dependencias para el correcto funcionamiento del proyecto.

### 4. Configuración de la base de datos

El proyecto utiliza una base de datos MySQL para almacenar la información de las leyendas. Para configurar la base de datos, sigue estos pasos:

#### 4.1 Crear la base de datos

Primero, asegúrate de que tienes MySQL instalado y corriendo en tu máquina. Luego, utiliza el script SQL proporcionado en el archivo `database_schema.sql` para crear la base de datos y las tablas necesarias.

1. **Conéctate a MySQL**:

   Abre una terminal y conéctate a MySQL con el siguiente comando:

   ```bash
   mysql -u tu_usuario -p
   ```

   Reemplaza `tu_usuario` con tu usuario de MySQL.

2. **Ejecuta el script SQL**:

   Asegúrate de estar en el directorio donde se encuentra el archivo `database_schema.sql` y ejecuta el siguiente comando para crear la base de datos:

   ```bash
   source database_schema.sql;
   ```

   Esto creará la base de datos `4thewords_prueba_kembly_munoz` y la tabla `leyendas` con algunos datos de ejemplo.

#### 4.2 Configurar la conexión a la base de datos

Crea un archivo `.env` en la raíz del proyecto con la siguiente variable de entorno:

```
DATABASE_URL=mysql://usuario:contraseña@localhost/4thewords_prueba_kembly_munoz
```

Reemplaza `usuario` y `contraseña` con tus credenciales de MySQL. Esto permitirá que el backend se conecte correctamente a la base de datos.

### 5. Levantar el servidor

Una vez que hayas configurado la base de datos y las variables de entorno, puedes levantar el servidor FastAPI utilizando **Uvicorn**.

```bash
uvicorn app.main:app --reload
```

Esto iniciará el servidor en modo desarrollo, lo que significa que se recargará automáticamente cada vez que realices cambios en el código.

- El servidor estará disponible en: `http://localhost:8000`
- El servidor estará disponible en: `http://localhost:8000`

### 6. Endpoints disponibles

A continuación se detallan los endpoints disponibles en la API:

- **`GET /leyendas`**: Obtiene todas las leyendas, con la opción de aplicar filtros.
  
  **Parámetros de consulta (query parameters):**
  - `nombre`: Filtra por nombre de la leyenda.
  - `categoria`: Filtra por categoría de la leyenda.
  - `fecha`: Filtra por fecha de la leyenda.
  - `provincia`: Filtra por provincia.
  - `canton`: Filtra por cantón.
  - `distrito`: Filtra por distrito.

  Ejemplo de uso: `http://localhost:8000/leyendas?nombre=La Llorona&provincia=San José`
  Ejemplo de uso: `http://localhost:8000/leyendas?nombre=La Llorona&provincia=San José`

- **`GET /leyendas/{id}`**: Obtiene una leyenda específica por su ID.

  Ejemplo de uso: `http://localhost:8000/leyendas/1`
  Ejemplo de uso: `http://localhost:8000/leyendas/1`

- **`POST /leyendas`**: Crea una nueva leyenda.
  
  **Cuerpo de la solicitud (JSON):**

  ```json
  {
    "nombre": "El Muerto",
    "categoria": "Leyenda urbana",
    "descripcion": "El alma errante de un hombre...",
    "fecha": "2024-07-20",
    "provincia": "San José",
    "canton": "Escazú",
    "distrito": "San Antonio",
    "imagen_url": "https://example.com/el-muerto.jpg"
  }
  ```

- **`PUT /leyendas/{id}`**: Actualiza una leyenda existente por su ID.

  **Cuerpo de la solicitud (JSON)**: Similar al cuerpo de la solicitud `POST`, pero incluye solo los campos que deseas actualizar.

- **`DELETE /leyendas/{id}`**: Elimina una leyenda por su ID.
ejemplo:
curl -X 'DELETE' \
  'http://localhost:8000/leyendas/10' \
  -H 'accept: application/json'

## Contacto

Si tienes alguna pregunta, no dudes en contactarme a través de [kemval@outlook.com].

---

### Créditos

- **Tecnologías utilizadas**:
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [SQLAlchemy](https://www.sqlalchemy.org/)
  - [MySQL](https://www.mysql.com/)
  - [Uvicorn](https://www.uvicorn.org/)
