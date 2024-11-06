from sqlalchemy import Column, String, Boolean,ARRAY
from models.base_model import BaseModel

class DNAModel(BaseModel):
    __tablename__ = 'dna_records'
    
    dna = Column(ARRAY(String), nullable=False)
    is_mutant = Column(Boolean, nullable=False)
