from pydantic import BaseModel
from typing import List

class DnaSchema(BaseModel):
    dna: List[str]
