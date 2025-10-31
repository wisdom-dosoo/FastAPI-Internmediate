from fastapi import FastAPI
from routers import post_op, get_op

app = FastAPI()

app.include_router(post_op.router)
app.include_router(get_op.router)


@app.get("/home")
def read_home():
    return {"message": "Welcome to the Home Page!"}

@app.get('/blog/all')
def get_all():
    return {'message': 'Get all blog from user request'}

@app.delete("/about")
def about():
    return {"response": 'This is the About Page.'}

@app.get("/blog/{id}")
def get_blogID():
    return {'message': "This blog ID"}

@app.post('/create/blog')    
def create_blog():
    return {'message': 'Blog created successfully!'}