from pydantic import BaseModel


class GlobalBase(BaseModel):
    class Config:
        pass
        # orm_mode = True #allows pydantic to work with SQLAlchemy models
        # add any other global model configs here
