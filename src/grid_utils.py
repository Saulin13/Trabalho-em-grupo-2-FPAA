"""
Utilitários para manipulação e leitura de grids.
"""


def create_empty_grid(n, m):
    """
    Cria um grid vazio (todos os valores são 0).
    
    Args:
        n: Número de linhas
        m: Número de colunas
    
    Returns:
        list: Grid n x m preenchido com zeros
    """
    return [[0 for _ in range(m)] for _ in range(n)]


def copy_grid(grid):
    """
    Cria uma cópia profunda do grid.
    
    Args:
        grid: Matriz 2D representando o grid
    
    Returns:
        list: Cópia do grid
    """
    return [row[:] for row in grid]


def find_first_zero(grid):
    """
    Encontra a primeira célula com valor 0 no grid.
    
    Args:
        grid: Matriz 2D representando o grid
    
    Returns:
        tuple: (x, y) da primeira célula com valor 0, ou None se não encontrar
    """
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                return (i, j)
    
    return None


def validate_grid(grid):
    """
    Valida se o grid tem formato válido.
    
    Args:
        grid: Matriz 2D representando o grid
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not grid:
        return False, "Grid vazio"
    
    if not isinstance(grid, list):
        return False, "Grid deve ser uma lista"
    
    n = len(grid)
    if n == 0:
        return False, "Grid deve ter pelo menos uma linha"
    
    if not isinstance(grid[0], list):
        return False, "Grid deve ser uma matriz 2D (lista de listas)"
    
    m = len(grid[0])
    if m == 0:
        return False, "Grid deve ter pelo menos uma coluna"
    
    # Verifica se todas as linhas têm o mesmo tamanho
    for i, row in enumerate(grid):
        if not isinstance(row, list):
            return False, f"Linha {i} não é uma lista"
        if len(row) != m:
            return False, f"Linha {i} tem tamanho diferente ({len(row)} vs {m})"
    
    return True, None

