from repositories.base_repository_impl import BaseRepositoryImpl
from repositories.dna_repository import DnaRepository
from models.dna_model import DNAModel
from schemas.dna_schema import DnaSchema
from services.dna_validator import DnaValidator

class DnaService(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(DnaRepository(), DNAModel, DnaSchema)

    def is_mutant(self, dna: list[str]) -> bool:
        validator = DnaValidator(dna)
        return validator.is_mutant()

    def save_dna(self, dna: list[str]) -> int:
        dna_schema = DnaSchema(sequence=dna)
        dna_instance = self.save(dna_schema)
        return dna_instance.id
