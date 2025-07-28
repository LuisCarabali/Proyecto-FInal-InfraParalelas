# api_service/Dockerfile

FROM python:3.12-slim

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crea carpeta app y copia archivos
WORKDIR /app
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
    ray[serve] fastapi uvicorn scikit-learn numpy

# Expone el puerto de la API
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
