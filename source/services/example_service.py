from source.schemas.example import ExampleCreate
from source.models.example import Example
from source.integrations.db.example import exampleDB
from source.integrations.db.database import get_db
from typing import List


class ExampleService:
    def __init__(self):
        self.example_db = exampleDB
        self.get_db = get_db

    def create_example(self, example_data: ExampleCreate) -> Example:
        """
        Be nice and add a lil description: Creates Example
        """
        example = Example(**example_data.dict())
        with self.get_db() as db:
            return self.example_db.save(db=db, example=example)

    def get_examples(self, names: List[str] = None) -> List[Example]:
        """
        Be nice and add a lil description: Gets Examples by name
        """
        with self.get_db() as db:
            examples, total = self.example_db.filter(db=db, names=names)
            return examples


exampleService = ExampleService()
