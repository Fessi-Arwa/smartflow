from fastapi import FastAPI

app = FastAPI(title="SmartFlow API")


@app.get("/")
def root():
    return {"message": "SmartFlow API is running!"}