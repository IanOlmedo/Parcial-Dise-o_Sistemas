from fastapi import APIRouter, HTTPException, Depends
from services.dna_service import DnaService
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.database import Database
from models.dna_model import DNAModel

router = APIRouter()

class DNARequest(BaseModel):
    dna: list[str]

@router.post("/mutant")
async def check_mutant(dna_request: DNARequest, db: Session = Depends(Database().get_session)):
    dna_service = DnaService()
    is_mutant = dna_service.is_mutant(dna_request.dna)
    
    # Verificar si el ADN ya está en la base de datos
    dna_record = db.query(DNAModel).filter(DNAModel.dna_sequence == dna_request.dna).first()
    
    if not dna_record:
        # Si el ADN no está en la base de datos, lo agregamos
        dna_record = DNAModel(dna_sequence=dna_request.dna, is_mutant=is_mutant)
        db.add(dna_record)
        db.commit()
    
    # Retornar resultado
    if is_mutant:
        return {"is_mutant": True}
    else:
        raise HTTPException(status_code=403, detail="Not a mutant")

@router.get("/stats")
async def get_stats(db: Session = Depends(Database().get_session)):
    count_mutant_dna = db.query(DNAModel).filter(DNAModel.is_mutant == True).count()
    count_human_dna = db.query(DNAModel).filter(DNAModel.is_mutant == False).count()
    ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0

    return {
        "count_mutant_dna": count_mutant_dna,
        "count_human_dna": count_human_dna,
        "ratio": ratio
    }

