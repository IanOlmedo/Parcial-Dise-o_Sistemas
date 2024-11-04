from fastapi import FastAPI
from controllers import dna_controller

app = FastAPI()

# Registrar el controlador de ADN
app.include_router(dna_controller.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al detector de mutantes"}

# Endpoint para verificar la salud de la aplicación
@app.get("/health_check")
def health_check():
    return {"status": "ok"}
