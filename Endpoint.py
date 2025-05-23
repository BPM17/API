from pydantic import BaseModel

class Endpoint(BaseModel):
    endpointName : str = None
    numberFields : int = None