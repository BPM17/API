from pydantic import BaseModel

class User(BaseModel):
    name : str = None
    lastName : str = None
    position : str = None