from fastapi import APIRouter
from schemas.dna_schema import DnaSchema
from services.dna_service import DnaService
from config.database import get_db

router = APIRouter()

class DnaController:
    # Define el endpoint de análisis de ADN
    @router.post("/mutant")
    async def analyze_dna(dna: DnaSchema):
        """Endpoint que analiza si el ADN es de un mutante."""
        service = DnaService()
        is_mutant = service.is_mutant(dna.sequence)
        service.save_dna(dna.sequence)  # Guarda el ADN
        return {"is_mutant": is_mutant}
