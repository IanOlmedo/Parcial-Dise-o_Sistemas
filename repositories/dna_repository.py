from typing import Type
from models.dna_model import DNAModel
from schemas.dna_schema import DnaSchema
from repositories.base_repository_impl import BaseRepositoryImpl

class DnaRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(DNAModel, DnaSchema)

    def save(self, dna_sequence: str, is_mutant: bool):
        dna_record = DNAModel(dna_sequence=dna_sequence, is_mutant=is_mutant)
        # Guarda el nuevo registro en la base de datos utilizando el método save heredado
        return super().save(dna_record)

    def get_all(self):
        # Devuelve todos los registros de la tabla DNAModel
        return super().find_all()
