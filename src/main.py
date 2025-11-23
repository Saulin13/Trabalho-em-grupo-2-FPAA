"""
Programa principal para demonstração do algoritmo Flood Fill.
"""

from flood_fill import fill_all_regions
from grid_utils import copy_grid, validate_grid
from visualization import print_grid_text, visualize_before_after


def exemplo_1():
    """
    Exemplo 1 do enunciado.
    """
    print("=" * 60)
    print("EXEMPLO 1")
    print("=" * 60)
    
    # Grid do exemplo 1
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    
    # Coordenadas iniciais
    start_x, start_y = 0, 0
    
    # Valida o grid
    is_valid, error = validate_grid(grid)
    if not is_valid:
        print(f"Erro: {error}")
        return
    
    # Cria uma cópia para não modificar o original
    grid_before = copy_grid(grid)
    
    # Mostra o grid antes
    print_grid_text(grid_before, "Grid ANTES do preenchimento")
    
    # Preenche todas as regiões
    result = fill_all_regions(grid, start_x, start_y)
    grid_after = result['grid']
    
    # Mostra o grid depois
    print_grid_text(grid_after, "Grid DEPOIS do preenchimento")
    
    # Estatísticas
    print(f"Regiões preenchidas: {result['regions_filled']}")
    print(f"Células preenchidas: {result['total_cells_filled']}")
    print(f"Cores usadas: {result['colors_used']}")
    
    # Visualização gráfica
    print("\nAbrindo visualização gráfica...")
    visualize_before_after(grid_before, grid_after, "exemplo1_resultado.png")


def exemplo_2():
    """
    Exemplo 2 do enunciado.
    """
    print("\n" + "=" * 60)
    print("EXEMPLO 2")
    print("=" * 60)
    
    # Grid do exemplo 2
    grid = [
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    
    # Coordenadas iniciais
    start_x, start_y = 0, 0
    
    # Valida o grid
    is_valid, error = validate_grid(grid)
    if not is_valid:
        print(f"Erro: {error}")
        return
    
    # Cria uma cópia para não modificar o original
    grid_before = copy_grid(grid)
    
    # Mostra o grid antes
    print_grid_text(grid_before, "Grid ANTES do preenchimento")
    
    # Preenche todas as regiões
    result = fill_all_regions(grid, start_x, start_y)
    grid_after = result['grid']
    
    # Mostra o grid depois
    print_grid_text(grid_after, "Grid DEPOIS do preenchimento")
    
    # Estatísticas
    print(f"Regiões preenchidas: {result['regions_filled']}")
    print(f"Células preenchidas: {result['total_cells_filled']}")
    print(f"Cores usadas: {result['colors_used']}")
    
    # Visualização gráfica
    print("\nAbrindo visualização gráfica...")
    visualize_before_after(grid_before, grid_after, "exemplo2_resultado.png")


def exemplo_customizado():
    """
    Exemplo customizado para demonstrar mais funcionalidades.
    """
    print("\n" + "=" * 60)
    print("EXEMPLO CUSTOMIZADO")
    print("=" * 60)
    
    # Grid customizado
    grid = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Coordenadas iniciais
    start_x, start_y = 0, 0
    
    # Valida o grid
    is_valid, error = validate_grid(grid)
    if not is_valid:
        print(f"Erro: {error}")
        return
    
    # Cria uma cópia para não modificar o original
    grid_before = copy_grid(grid)
    
    # Mostra o grid antes
    print_grid_text(grid_before, "Grid ANTES do preenchimento")
    
    # Preenche todas as regiões
    result = fill_all_regions(grid, start_x, start_y)
    grid_after = result['grid']
    
    # Mostra o grid depois
    print_grid_text(grid_after, "Grid DEPOIS do preenchimento")
    
    # Estatísticas
    print(f"Regiões preenchidas: {result['regions_filled']}")
    print(f"Células preenchidas: {result['total_cells_filled']}")
    print(f"Cores usadas: {result['colors_used']}")
    
    # Visualização gráfica
    print("\nAbrindo visualização gráfica...")
    visualize_before_after(grid_before, grid_after, "exemplo_customizado_resultado.png")


def main():
    """
    Função principal do programa.
    """
    print("\n" + "=" * 60)
    print("ALGORITMO FLOOD FILL - Trabalho FPAA")
    print("=" * 60)
    print("\nEste programa demonstra o algoritmo Flood Fill")
    print("para preenchimento de regiões em um grid 2D.\n")
    
    # Executa os exemplos
    exemplo_1()
    exemplo_2()
    exemplo_customizado()
    
    print("\n" + "=" * 60)
    print("Execução concluída!")
    print("=" * 60)


if __name__ == "__main__":
    main()

