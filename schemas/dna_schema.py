from pydantic import BaseModel
from typing import List

class DnaSchema(BaseModel):
    dna_sequence: List[str]
