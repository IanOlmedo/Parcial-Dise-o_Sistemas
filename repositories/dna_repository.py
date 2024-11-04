from sqlalchemy.orm import Session
from models.dna_model import DNAModel

class DnaRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, dna_sequence, is_mutant):
        dna_record = DNAModel(dna_sequence=dna_sequence, is_mutant=is_mutant)
        self.db.add(dna_record)
        self.db.commit()

    def get_all(self):
        return self.db.query(DNAModel).all()
