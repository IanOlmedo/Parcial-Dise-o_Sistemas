class DnaService:
    def is_mutant(self, dna):
        # Implementación de la lógica para detectar secuencias de 4 letras iguales
        # (horizontal, vertical o diagonal) en la matriz `dna`
        n = len(dna)
        sequences_found = 0

        def check_sequence(x, y, dx, dy):
            # Verifica una secuencia de 4 letras en la dirección dada
            base = dna[x][y]
            for _ in range(1, 4):
                x += dx
                y += dy
                if x >= n or y >= n or dna[x][y] != base:
                    return False
            return True

        # Buscar secuencias horizontales, verticales y diagonales
        for i in range(n):
            for j in range(n):
                if dna[i][j] and (
                    (j <= n - 4 and check_sequence(i, j, 0, 1)) or  # Horizontal
                    (i <= n - 4 and check_sequence(i, j, 1, 0)) or  # Vertical
                    (i <= n - 4 and j <= n - 4 and check_sequence(i, j, 1, 1)) or  # Diagonal \
                    (i >= 3 and j <= n - 4 and check_sequence(i, j, -1, 1))  # Diagonal /
                ):
                    sequences_found += 1
                if sequences_found > 1:
                    return True
        return False
