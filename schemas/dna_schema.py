from pydantic import BaseModel
from typing import List

class DnaRequest(BaseModel):
    dna_sequence: List[str]
    is_mutant: bool
