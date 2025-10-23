from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class PredefinedPath(str, Enum):
    short = 'short'
    blog_all = 'get_all'
    about = 'about'
    blog_id = 'blog_id'
    create_blog = 'create_blog'
   
@app.get('/predefined/{path_name}')
def get_predefined_path(path_name: PredefinedPath):
    return {'message': f'The predefined path is: {path_name.value}'}