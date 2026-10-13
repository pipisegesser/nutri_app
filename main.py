import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException
# ... resto de tus imports ...
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NutriApp Local", version="1.0")

# Montamos la carpeta static para servir la interfaz web
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/pacientes/", response_model=schemas.PacienteResponse)
def crear_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = db.query(models.Paciente).filter(models.Paciente.email == paciente.email).first()
    if db_paciente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado para otro paciente.")
    
    nuevo_paciente = models.Paciente(**paciente.dict())
    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)
    return nuevo_paciente

@app.get("/pacientes/", response_model=list[schemas.PacienteResponse])
def listar_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = db.query(models.Paciente).offset(skip).limit(limit).all()
    return pacientes