from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models, schemas
from datetime import date

# si no están creadas, crea las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# inicia la app de FastAPI
app = FastAPI()

# función me da la sesión de la base de datos para que la pueda usar
def get_db():
    db = SessionLocal()  # Abro una sesión
    try:
        yield db  # devuelvo la sesión para que se use
    finally:
        db.close()  # cierra la sesión para liberar recursos

# endpoint para obtener leyendas, filtrarlas por varios parámetros
@app.get("/leyendas", response_model=list[schemas.Leyenda])
def obtener_leyendas(
    db: Session = Depends(get_db),  # solicito la sesión de la base de datos
    nombre: str = Query(None, alias="nombre", max_length=100),  # Filtro por nombre si lo paso
    categoria: str = Query(None, alias="categoria", max_length=50),  # Filtro por categoría si lo paso
    fecha: date = Query(None, alias="fecha"),  # Puedo filtrar también por fecha
    provincia: str = Query(None, alias="provincia", max_length=50),  # Filtro por provincia
    canton: str = Query(None, alias="canton", max_length=50),  # Filtro por cantón
    distrito: str = Query(None, alias="distrito", max_length=50)  # Filtro por distrito
):
    query = db.query(models.Leyenda)  # Empiezo la consulta para obtener leyendas

    # Aplico los filtros que se pasan como parámetros
    if nombre:
        query = query.filter(models.Leyenda.nombre.ilike(f"%{nombre}%"))
    if categoria:
        query = query.filter(models.Leyenda.categoria.ilike(f"%{categoria}%"))
    if fecha:
        query = query.filter(models.Leyenda.fecha == fecha)
    if provincia:
        query = query.filter(models.Leyenda.provincia.ilike(f"%{provincia}%"))
    if canton:
        query = query.filter(models.Leyenda.canton.ilike(f"%{canton}%"))
    if distrito:
        query = query.filter(models.Leyenda.distrito.ilike(f"%{distrito}%"))

    return query.all()  # Devuelvo todas las leyendas que coinciden con los filtros

# endpoint obtiene una leyenda específica por su ID
@app.get("/leyendas/{id}", response_model=schemas.Leyenda)
def obtener_leyenda(id: int, db: Session = Depends(get_db)):
    leyenda = db.query(models.Leyenda).filter(models.Leyenda.id == id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")  # Si no la encuentro, devuelvo error
    return leyenda  # Si la encuentro, la devuelvo

# endpoint para crear una leyenda nueva
@app.post("/leyendas", response_model=schemas.Leyenda)
def crear_leyenda(leyenda: schemas.LeyendaCreate, db: Session = Depends(get_db)):
    nueva_leyenda = models.Leyenda(**leyenda.dict())  # Creo la leyenda con los datos que recibí
    db.add(nueva_leyenda)  # La agrego a la base de datos
    db.commit()  # Guardo los cambios
    db.refresh(nueva_leyenda)  # Actualizo la leyenda con los datos de la base de datos
    return nueva_leyenda  # Retorno la leyenda recién creada

@app.put("/leyendas/{leyenda_id}", response_model=schemas.Leyenda)
def actualizar_leyenda(leyenda_id: int, leyenda_actualizada: schemas.LeyendaCreate, db: Session = Depends(get_db)):
    leyenda = db.query(models.Leyenda).filter(models.Leyenda.id == leyenda_id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    for key, value in leyenda_actualizada.dict().items():
        setattr(leyenda, key, value)
    db.commit()
    db.refresh(leyenda)
    return leyenda

@app.delete("/leyendas/{leyenda_id}")
def eliminar_leyenda(leyenda_id: int, db: Session = Depends(get_db)):
    leyenda = db.query(models.Leyenda).filter(models.Leyenda.id == leyenda_id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    db.delete(leyenda)
    db.commit()
    return {"message": "Leyenda eliminada correctamente"}
