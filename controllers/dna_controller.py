from fastapi import APIRouter, HTTPException
from services.dna_service import DnaService
from pydantic import BaseModel

router = APIRouter()

class DNARequest(BaseModel):
    dna: list[str]


@router.post("/mutant")
async def check_mutant(dna_request: DNARequest):
    dna_service = DnaService()
    
    # Llama al método `is_mutant` para determinar si el ADN pertenece a un mutante
    if dna_service.is_mutant(dna_request.dna):
        return {"is_mutant": True}
    else:
        # Si no es mutante, lanza una excepción con código de estado 403
        raise HTTPException(status_code=403, detail="Not a mutant")

