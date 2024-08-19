from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from source.models.example import Example
from uuid import UUID


class ExampleDB:
    def save(self, db: Session, example: Example):
        db.add(example)
        db.commit()
        db.refresh(example)
        return example

    # an example of a paginated filter function
    def filter(
        self,
        db: Session,
        ids: Optional[List[UUID]] = None,
        names: Optional[List[str]] = None,
        page: int = 1,
        page_size: int = 10,
    ) -> Tuple[List[Example], int]:
        q = db.query(Example)
        if ids:
            q = q.filter(Example.id.in_(ids))
        if names:
            q = q.filter(Example.name.in_(names))

        total = q.count()
        examples = q.offset((page - 1) * page_size).limit(page_size).all()

        return examples, total


exampleDB = ExampleDB()
