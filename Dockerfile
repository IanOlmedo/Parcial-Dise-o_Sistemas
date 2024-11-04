# Usa una imagen oficial de Python como base para la etapa de construcción
FROM python:3.11.6-slim-bullseye AS builder

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias en la capa de construcción
RUN pip install --no-cache-dir --user -r requirements.txt

# Inicia una nueva etapa con una imagen más ligera
FROM python:3.11.6-slim-bullseye

# Copia las dependencias instaladas en la etapa anterior
COPY --from=builder /root/.local /root/.local

# Asegura que los scripts en .local sean utilizables
ENV PATH=/root/.local/bin:$PATH

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Expone el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación de FastAPI usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
