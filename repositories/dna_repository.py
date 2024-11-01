class DnaRepository:
    def __init__(self):
        self.data = []

    def save(self, dna_sequence, is_mutant):
        # Guarda la secuencia de ADN y si es mutante
        self.data.append({"dna": dna_sequence, "is_mutant": is_mutant})
    
    def get_all(self):
        return self.data
