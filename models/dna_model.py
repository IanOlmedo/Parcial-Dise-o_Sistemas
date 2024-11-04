from sqlalchemy import Column, String, Boolean
from models.base_model import Base

class DNAModel(Base):
    __tablename__ = 'dna_records'
    
    dna_sequence = Column(String, primary_key=True, unique=True, nullable=False)
    is_mutant = Column(Boolean, nullable=False)
