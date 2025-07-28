🧠 Proyecto Final - Infraestructuras Paralelas y Distribuidas

**Estudiante:** Luis Carabalí, Victor Acuña, Nicolas Granada.  
**Universidad del Valle**  
**Curso:** Infraestructura Paralela y Distribuida  
**Tema:** Machine Learning paralelo con Ray, FastAPI, Docker y despliegue en AWS EC2

---

## 🎯 Objetivo

Implementar y comparar una solución de clasificación con Machine Learning ejecutada en forma **secuencial** y **paralela**, desplegando la solución como un microservicio en la nube.

---

## 🛠️ Tecnologías utilizadas

- 🐍 Python 3
- 🤖 scikit-learn
- ⚡ Ray (paralelismo)
- 🚀 FastAPI
- 🐳 Docker + Docker Compose
- ☁️ AWS EC2
- 🐙 GitHub

---

## ⚙️ Estructura del proyecto

Proyecto-Final/
│
├── ray_parallel/ # Entrenamiento en paralelo usando Ray
│ └── train_model.py
│
├── sequential/ # Entrenamiento secuencial
│ └── train_model.py
│
├── api_service/ # API con FastAPI para predicción
│ └── main.py
│
├── docker-compose.yml # Orquestación de servicios
├── README.md
└── .gitignore


---

## 🧪 Instrucciones de uso

### 🧱 Requisitos

- Python 3.10 o superior
- Docker y Docker Compose
- Git

### 🚀 Entrenamiento local

Secuencial:

```bash
python3 sequential/train_model.py


---

## 🧪 Instrucciones de uso

### 🧱 Requisitos

- Python 3.10 o superior
- Docker y Docker Compose
- Git

### 🚀 Entrenamiento local

Secuencial:

```bash
python3 sequential/train_model.py

python3 ray_parallel/train_model.py

cd api_service
docker build -t ray-api .
docker run -p 8000:8000 ray-api

Accede en: http://localhost:8000/docs

☁️ Despliegue en AWS EC2
Subir el proyecto con scp

Instalar dependencias (docker, python3, etc.)

Ejecutar: docker-compose up --build -d

Accede en: http://13.59.51.54:8000/docs

📊 Resultados
Versión	Precisión	Tiempo aprox
Secuencial	0.9759	~0.4 s
Paralelo	0.9750	~2.4 s

Nota: En instancias t3.micro fue necesario reducir el tamaño del dataset y ajustar los parámetros de Ray para evitar errores de memoria.

✅ Conclusiones
Se implementó exitosamente el paralelismo con Ray.

Se desplegó una API funcional en la nube con Docker.

Se evaluó rendimiento entre ejecución secuencial vs. paralela.

Se usaron herramientas reales de DevOps y ML como en entornos profesionales.
