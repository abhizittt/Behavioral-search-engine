from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Behavioral Search Engine is running"}