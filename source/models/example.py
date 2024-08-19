from sqlalchemy import Column, Integer, String, Text
from source.integrations.db.database import Base


class Example(Base):
    __tablename__ = "example_table"

    id = Column(
        Integer, primary_key=True, index=True
    )  # TODO: better to do id: Mapped[UUID] = mapped_column(saUUID, primary_key=True, default=uuid7)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
