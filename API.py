from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from GirdiBurg import signup, validar_email

app = FastAPI(title="Gordibug api", version="2.0")

MENU_ITEMS = {
    "hamburguesa": "35.00",
    "hot dog": "25.00",
    "refresco": "20.00",
    "agua fresca": "20.00"
}

class Registro (BaseModel):
    usuario: str = Field(min_length=1, max_length=10, description="Nombre de usuario")
    email: str = Field(min_length=1, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$', description="Correo electrónico válido")

@app.get("/menu")
def get_menu():
    return {"menu":MENU_ITEMS}

@app.post("/registro")
def post_registro(data: Registro):
    if not signup(data.email):
        raise HTTPException(status_code=400, detail="Correo electrónico inválido")