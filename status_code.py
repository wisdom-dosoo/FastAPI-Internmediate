from fastapi import FastAPI
from fastapi import status, Response 

app = FastAPI()

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_id(id: int, response: Response):
    if id > 10:
        response.status_code = status.NOT_FOUND
        return {'error': 'Blog {id} not found'}
    else:    
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with ID {id} fetched successfully!'}