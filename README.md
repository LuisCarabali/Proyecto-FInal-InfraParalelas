
# Proyecto Final – Infraestructuras Paralelas y Distribuidas 🧠⚙️

Este proyecto implementa un sistema de entrenamiento de modelos de Machine Learning usando Ray para paralelismo, y FastAPI como microservicio, todo empaquetado en Docker y desplegado en una instancia EC2 de AWS.

---

## 📂 Estructura del Proyecto

```
Proyecto-Final/
├── api_service/               # Microservicio con FastAPI
│   ├── main.py
│   └── Dockerfile
├── ray_parallel/              # Modelo paralelo con Ray
│   └── train_model.py
├── sequential/                # Modelo secuencial
│   └── train_model.py
├── docker-compose.yml         # Orquestador de contenedores
└── venv/                      # Entorno virtual (local)
```

---

## ⚙️ Requisitos

- Python 3.10+
- Docker y Docker Compose
- AWS EC2 con Ubuntu 22.04
- Clave `.pem` para acceso SSH

---

## 🚀 Ejecución Local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python sequential/train_model.py
python ray_parallel/train_model.py
```

---

## 🐳 Docker

```bash
docker-compose up --build -d
```
API disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☁️ Despliegue en EC2

```bash
ssh -i "luis-ec2-key.pem" ubuntu@<IP_PUBLICA>
scp -i "luis-ec2-key.pem" -r Proyecto-Final ubuntu@<IP_PUBLICA>:/home/ubuntu/
cd Proyecto-Final
docker-compose up --build -d
```

---

## 🔍 Uso del Microservicio

**POST /predict**  
Cuerpo:
```json
{
  "features": [64 valores]
}
```

Respuesta:
```json
{
  "predicted_class": 3
}
```

---

## 📊 Comparación de Resultados

| Versión         | Precisión | Tiempo (s) |
|-----------------|-----------|------------|
| Secuencial      | 0.9704    | 0.3598     |
| Paralelo (Ray)  | 0.9750    | 2.4636     |

---

## 📄 Autor

Desarrollado por **Luis Carabalí** – Universidad del Valle 🇨🇴  
Proyecto final del curso **Infraestructuras Paralelas y Distribuidas**
