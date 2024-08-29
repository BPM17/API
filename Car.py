from pydantic import BaseModel

class Car(BaseModel):
    id : int = None
    brand : str = None
    model : str = None
    color : str = None
    year : int  = None