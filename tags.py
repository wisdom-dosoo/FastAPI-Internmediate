from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_home():
    return {"message": "Welcome to the Home Page!"}

@app.get('/blog/all', tags=['blogs'])
def get_all():
    return {'message': 'Get all blog from user request'}

@app.delete("/about", tags=['info'])
def about():
    return {"response": 'This is the About Page.'}

@app.get("/blog/{id}", tags=['blogs'])
def get_blogID():
    return {'message': "This blog ID"}

@app.post('/create/blog', tags=['creation'])
def create_blog():
    return {'message': 'Blog created successfully!'}