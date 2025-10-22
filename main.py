from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_home():
    return {"message": "Welcome to the Home Page!"}

@app.get("/about")
def about():
    return {"response": 'This is the About Page.'}
