from fastapi import APIRouter, HTTPException
from services.dna_service import DnaService
from schemas.dna_schema import DnaRequest

router = APIRouter()

@router.post("/mutant/")
async def is_mutant(dna_request: DnaRequest):
    dna_service = DnaService()
    is_mutant = dna_service.is_mutant(dna_request.dna)
    if is_mutant:
        return {"message": "Es un mutante"}
    else:
        raise HTTPException(status_code=403, detail="No es un mutante")
