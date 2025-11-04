import uvicorn
from fastapi import FastAPI

# Instance of FastAPI object
app = FastAPI()

# Home Page for web server
@app.get("/")
def home_page():
    return "Welcome to the Book Recommender"


