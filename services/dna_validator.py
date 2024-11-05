from typing import List

class DnaValidator:
    def __init__(self, dna: List[str]):
        self.dna = dna
        self.size = len(dna)

    def is_mutant(self) -> bool:
        # Lista de direcciones para la búsqueda: horizontal, vertical, diagonal descendente, diagonal ascendente
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        
        # Generador para contar secuencias mutantes
        sequences_found = sum(
            1 for i in range(self.size) for j in range(self.size)
            if any(self._has_sequence(i, j, dx, dy) for dx, dy in directions)
        )
        
        return sequences_found > 1

    def _has_sequence(self, x: int, y: int, dx: int, dy: int) -> bool:
        """Verifica si hay una secuencia de 4 letras en una dirección dada (dx, dy)"""
        try:
            base = self.dna[x][y]
            return all(
                self.dna[x + k * dx][y + k * dy] == base
                for k in range(4)
            )
        except IndexError:
            return False
