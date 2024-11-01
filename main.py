from fastapi import FastAPI
from controllers import dna_controller

app = FastAPI()

# Registrar el controlador de ADN
app.include_router(dna_controller.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al detector de mutantes"}
