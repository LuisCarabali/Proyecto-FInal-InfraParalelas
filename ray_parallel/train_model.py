# ray_parallel/train_model.py

import ray
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

@ray.remote
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def main():
    # Cargar datos (parecido a MNIST)
    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42)

    ray.init()  # inicia Ray

    # Entrenar modelo en paralelo
    future_model = train_model.remote(X_train, y_train)
    model = ray.get(future_model)

    # Evaluar
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Precisión: {acc:.4f}")

    ray.shutdown()

if __name__ == "__main__":
    main()
