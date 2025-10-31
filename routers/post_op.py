from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/post_op",
    tags=["post_op"]
)

@router.post('/')
def create_post():
    return {"message": f'Post created successfully.'}

@router.post('/{post_id}')
def read_post(post_id: int):
    return {"message": f'Retrieved post with ID {post_id}.'}    