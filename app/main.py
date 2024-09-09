from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import pandas as pd
import sys
import os

# Agregar la carpeta 'app/' al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '.app/'))
from app.utils.utils import calc_top_methodologies_and_techniques, get_results
from app.schemas import InnovacionFormularioCreate

app = FastAPI()

class RequestData(BaseModel):
    proposito_iniciativa: list[str]
    fase_innovacion: list[str]
    urgencia: int
    complejidad: int
    incertidumbre: int
    colaboracion: int
    recursos: int
    flexibilidad: int
    velocidad: int
    riesgo: int
    usuario: int
    

@app.post("/calculate/")
async def calculate(data: RequestData):
    try:
        result = get_results(data.dict())  # Asegúrate de pasar el dict y no el RequestData directamente
        return result
    except Exception as e:
        print(f"Error durante la solicitud: {e}")
        raise HTTPException(status_code=500, detail=f"Error procesando la solicitud: {str(e)}")
