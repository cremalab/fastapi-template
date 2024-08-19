from fastapi import APIRouter
from source.schemas.example import ExampleCreate, ExampleResponse
from source.services.example_service import exampleService

from typing import List

router = APIRouter()


@router.post("/", response_model=ExampleResponse)
def create_example(example: ExampleCreate):
    return exampleService.create_example(example_data=example)


@router.get("/", response_model=List[ExampleResponse])
def list_examples(names: List[str] = None):
    return exampleService.get_examples(names=names)
