from typing import Union

from fastapi import FastAPI

app = FastAPI()

#ruta Raiz
@app.get("/")
def read_root():
    return {"Hello": "World"}

#las rutas le dice poe, endpoit
#ruta items y pide un parametro numerico, 
# tambien se puede anexar un valor string que es opcional
# ejemplo: http://127.0.0.1:8000/items/10?q=mouse
# R. {"item_id":10,"q":"mouse"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#ejemplo de una calculadora que sume
@app.get("/suma")
def sumar(operador1:float,operador2:float):
    return {'suma':operador1+operador2}
