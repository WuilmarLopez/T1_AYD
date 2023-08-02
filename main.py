from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class numeros(BaseModel):
    numero1: int
    numero2: int

@app.get("/")
def index():
    return {"message": "Hello World"}


#poniendo el metodo de suma
@app.post("/post")
def post(numero: numeros):
    return {"suma": f"{numero.numero1 + numero.numero2}"}
