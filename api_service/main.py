# api_service/main.py

import ray
from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Entrenar modelo al arrancar
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# FastAPI
app = FastAPI()

class InputData(BaseModel):
    image: list

@app.post("/predict")
def predict(data: InputData):
    x = np.array(data.image).reshape(1, -1)
    prediction = model.predict(x)[0]
    return {"predicted_class": int(prediction)}

# Inicializamos Ray Serve
if __name__ == "__main__":
    ray.init()
    serve.run(app, route_prefix="/")
