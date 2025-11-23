"""
Implementação do algoritmo Flood Fill usando DFS (Depth-First Search).
"""


def flood_fill(grid, x, y, color):
    """
    Preenche uma região conectada de células com valor 0 usando Flood Fill.
    
    O algoritmo usa DFS (Depth-First Search) para percorrer todas as células
    conectadas ortogonalmente (cima, baixo, esquerda, direita) que têm valor 0,
    preenchendo-as com a cor especificada.
    
    Args:
        grid: Matriz 2D representando o grid (lista de listas)
        x: Coordenada x (linha) inicial
        y: Coordenada y (coluna) inicial
        color: Valor da cor para preencher (int >= 2)
    
    Returns:
        int: Número de células preenchidas
    """
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    # Validação de entrada
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    # Se a célula inicial não é navegável (0), não faz nada
    if grid[x][y] != 0:
        return 0
    
    # Pilha para DFS
    stack = [(x, y)]
    filled_count = 0
    
    # Enquanto houver células para processar
    while stack:
        curr_x, curr_y = stack.pop()
        
        # Verifica se a célula ainda precisa ser preenchida
        if grid[curr_x][curr_y] != 0:
            continue
        
        # Preenche a célula com a cor
        grid[curr_x][curr_y] = color
        filled_count += 1
        
        # Adiciona vizinhos ortogonais à pilha
        # Direções: cima, baixo, esquerda, direita
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x = curr_x + dx
            new_y = curr_y + dy
            
            # Verifica se está dentro dos limites e se é navegável (0)
            if (0 <= new_x < n and 0 <= new_y < m and 
                grid[new_x][new_y] == 0):
                stack.append((new_x, new_y))
    
    return filled_count


def fill_all_regions(grid, start_x, start_y):
    """
    Preenche todas as regiões navegáveis do grid automaticamente.
    
    Começa preenchendo a região que contém (start_x, start_y) com a cor 2.
    Depois, procura automaticamente por outras células com valor 0 e preenche
    cada região encontrada com cores subsequentes (3, 4, 5, ...).
    
    Args:
        grid: Matriz 2D representando o grid (lista de listas)
        start_x: Coordenada x (linha) inicial
        start_y: Coordenada y (coluna) inicial
    
    Returns:
        dict: Estatísticas do preenchimento (número de regiões, células preenchidas, etc.)
    """
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    # Cria uma cópia do grid para não modificar o original
    grid_copy = [row[:] for row in grid]
    
    # Preenche a região inicial com cor 2
    initial_filled = flood_fill(grid_copy, start_x, start_y, 2)
    
    # Contadores
    current_color = 3
    regions_filled = 1 if initial_filled > 0 else 0
    total_cells_filled = initial_filled
    
    # Procura por outras células com valor 0 e preenche
    for i in range(n):
        for j in range(m):
            if grid_copy[i][j] == 0:
                # Encontrou uma nova região, preenche com a próxima cor
                cells_filled = flood_fill(grid_copy, i, j, current_color)
                if cells_filled > 0:
                    regions_filled += 1
                    total_cells_filled += cells_filled
                    current_color += 1
    
    return {
        'grid': grid_copy,
        'regions_filled': regions_filled,
        'total_cells_filled': total_cells_filled,
        'colors_used': current_color - 2  # Número de cores usadas (começa em 2)
    }

