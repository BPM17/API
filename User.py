from pydantic import BaseModel

class User(BaseModel):
    name : str = None
    lastName : str = None
    email : str = None
    password : str = None
    position : str = None