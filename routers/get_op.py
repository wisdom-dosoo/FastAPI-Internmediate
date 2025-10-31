from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/get_op",
    tags=["get_op"]
)
@router.get('/')
def read_root():
    return {"message": f'Get operation root endpoint.'}

@router.get('/{item_id}')
def read_item(item_id: int):
    return {"message": f'Retrieved item with ID {item_id}.'}

@router.get('/all')
def read_all_items():
    return {"message": 'Retrieved all items.'}

@router.get('/search/')            
def search_items(query: str):
    return {"message": f'Search results for query: {query}.'}
