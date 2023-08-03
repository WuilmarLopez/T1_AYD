from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class numeros(BaseModel):
    numero1: int
    numero2: int

@app.get("/")
def index():
    return {"message": "Hello World"}


#poniendo el metodo de multiplicacion
@app.post("/post")
def post(numero: numeros):
    return {"multiplicacion": f"{numero.numero1 * numero.numero2}"}

#poniendo el metodo de info
@app.get("/info")
def info():
    return {"info": "201901069"}
