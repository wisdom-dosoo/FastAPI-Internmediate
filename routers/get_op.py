from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/get_op",
    tags=["get_op"]
)

class Item (BaseModel):
    title: str
    description: str = None
    container: str
    published: bool = True

@router.get('/{item_id}')
def read_item(item_id: int):
    return {"message": f'Retrieved item with ID {item_id}.'}

@router.get('/all')
def read_all_items(get: Item):
    return {"message": 'Retrieved all items.'}

@router.get('/search/')            
def search_items(query: Item):
    return {"message": f'Search results for query: {query}.'}


@router.get('/')
def read_root():
    return {"message": f'Get operation root endpoint.'}