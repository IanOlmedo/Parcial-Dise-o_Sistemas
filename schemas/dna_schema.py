from pydantic import BaseModel
from typing import List

class DnaRequest(BaseModel):
    dna: List[str]
