# main.py

import uvicorn
from fastapi import FastAPI, Depends
from starlette import status
from starlette.responses import JSONResponse

from config.database import Database, get_db
from controllers.dna_controller import router as dna_controller
from repositories.base_repository_impl import InstanceNotFoundError


def create_fastapi_app():
    """Crea y configura la aplicación FastAPI."""
    fastapi_app = FastAPI()

    # Manejador de excepciones personalizadas
    @fastapi_app.exception_handler(InstanceNotFoundError)
    async def instance_not_found_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": str(exc)},
        )

    # Registro de routers
    fastapi_app.include_router(dna_controller, prefix="/dna")

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    """Ejecuta la aplicación en el servidor uvicorn."""
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Inicialización de la base de datos y tablas
    db = Database()
    if db.check_connection():
        db.create_tables()

    # Creación y ejecución de la aplicación
    app = create_fastapi_app()
    run_app(app)

