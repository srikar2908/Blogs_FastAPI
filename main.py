from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hello i am srikar"

@app.get("/about")
def about():
    return "i am srikar i am from india"