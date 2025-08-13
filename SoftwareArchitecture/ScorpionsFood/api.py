
#todo: Correrlo en consola: uvicorn api:app --reload

#todo: en el navegador: http://127.0.0.1:8000/menu
#todo:API: http://127.0.0.1:8000
#todo: Docs interactivas: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from App_Scorpionsfood import validar_email

app = FastAPI(title="Gordiburg API", version="2.0")

# Re-declaramos el menú aquí para NO modificar el base.
MENU_ITEMS = {
    "hamburguesa": "35.00",
    "hot dog": "25.00",
    "refresco": "20.00",
    "agua fresca": "20.00"
}

class Registro(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del usuario")
    email: str = Field(min_length=5, description="Correo electrónico a validar")

@app.get("/menu")
def get_menu():
    return {"menu": MENU_ITEMS}

@app.post("/registro")
def post_registro(data: Registro):
    if not validar_email(data.email):
        raise HTTPException(status_code=400, detail="Correo electrónico inválido")
    
    #!Aquí podrías guardar en una BD; por ahora devolvemos OK.
    return {"status": "ok", "mensaje": f"Usuario '{data.nombre}' registrado con éxito."}
