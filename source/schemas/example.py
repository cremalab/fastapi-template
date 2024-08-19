# import GlobalBase
from .base import GlobalBase
from typing import Optional


class ExampleBase(GlobalBase):
    name: str
    description: Optional[str] = None


# validate data sent by clients when creating new records
class ExampleCreate(ExampleBase):
    pass


# Define structure of data returned to client
class ExampleResponse(ExampleBase):
    id: int
