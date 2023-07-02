from pydantic import BaseModel
from typing import Union

#vamos a tabajar con un tipo de datos y usaremos
# el modelo BaseModel y put para actualizar datos 
# atravez de la libreria pydantic del modelo BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None