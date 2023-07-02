from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#ruta Raiz
@app.get("/")
def read_root():
    return {"Hello": "World"}

#las rutas le dice poe, endpoit
#ruta items y pide un parametro numerico, 
# tambien se puede anexar un valor string que es opcional.
# ejemplo: http://127.0.0.1:8000/items/10?q=mouse
# R. {"item_id":10,"q":"mouse"}
# {item_id} es un parametro de ruta.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#endpoint de una calculadora que sume
#ejemplo http://127.0.0.1:8000/suma?operador1=6&operador2=3
#R. {"suma":9.0}
#operador1 y operador2 son parametros de entradas llamadas 
# tambien query params. parametros de consulta
@app.get("/suma")
def sumar(operador1:float,operador2:float):
    return {'suma':operador1+operador2}


"""
 Tipos de parametros de una ruta:
    * Ruta /
    * Consulta ?,&

 Get   -> consultar
 Put   -> actualizar
 Post  -> crear
 Delet -> borrar

"""

#vamos a tabajar con un tipo de datos y usaremos
# el modelo BaseModel y put para actualizar datos 
# atravez de la libreria pydantic del modelo BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offert: Union(bool,None) = None