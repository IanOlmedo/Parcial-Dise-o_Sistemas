class DnaService:
    def is_mutant(self, dna: list[str]) -> bool:
        n = len(dna)
        sequences_found = 0

        def check_sequence(x, y, dx, dy):
            # Verifica una secuencia de 4 letras en la dirección dada
            base = dna[x][y]
            for _ in range(1, 4):
                x += dx
                y += dy
                if x < 0 or x >= n or y < 0 or y >= n or dna[x][y] != base:
                    return False
            return True

        # Buscar secuencias de cuatro letras en cada dirección
        for i in range(n):
            for j in range(n):
                if (
                    (j <= n - 4 and check_sequence(i, j, 0, 1)) or  # Horizontal
                    (i <= n - 4 and check_sequence(i, j, 1, 0)) or  # Vertical
                    (i <= n - 4 and j <= n - 4 and check_sequence(i, j, 1, 1)) or  # Diagonal descendente \
                    (i >= 3 and j <= n - 4 and check_sequence(i, j, -1, 1))  # Diagonal ascendente /
                ):
                    sequences_found += 1
                if sequences_found > 1:
                    return True
        return False
