from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Cloud Run!"}

@app.get("/predict")
def predict():
    return {"prediction": 42}
