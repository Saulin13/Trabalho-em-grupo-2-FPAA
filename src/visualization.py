"""
Módulo para visualização do grid em formato texto e gráfico.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
import numpy as np


def print_grid_text(grid, title="Grid"):
    """
    Imprime o grid no terminal em formato texto.
    
    Args:
        grid: Matriz 2D representando o grid
        title: Título para exibir antes do grid
    """
    print(f"\n{title}:")
    print("-" * (len(grid[0]) * 3 + 1))
    
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell} ", end="")
        print("|")
    
    print("-" * (len(grid[0]) * 3 + 1))
    print()


def get_color_map():
    """
    Retorna um mapa de cores para os valores do grid.
    
    Returns:
        dict: Mapa de valores para cores (nome da cor matplotlib)
    """
    # Cores para diferentes valores
    # 0 = branco, 1 = preto, 2+ = cores do espectro
    color_map = {
        0: 'white',
        1: 'black',
    }
    
    # Cores para valores >= 2 (regiões preenchidas)
    colors_list = [
        'red',      # 2
        'orange',   # 3
        'yellow',   # 4
        'green',    # 5
        'cyan',     # 6
        'blue',     # 7
        'purple',   # 8
        'pink',     # 9
        'brown',    # 10
        'gray',     # 11
    ]
    
    # Adiciona cores para valores maiores (reutiliza cores se necessário)
    for i in range(2, 100):  # Suporta até 100 cores diferentes
        if i - 2 < len(colors_list):
            color_map[i] = colors_list[i - 2]
        else:
            # Reutiliza cores em ciclo
            color_map[i] = colors_list[(i - 2) % len(colors_list)]
    
    return color_map


def visualize_grid_graphic(grid, title="Grid", save_path=None):
    """
    Visualiza o grid graficamente usando matplotlib.
    
    Args:
        grid: Matriz 2D representando o grid
        title: Título do gráfico
        save_path: Caminho opcional para salvar a imagem (ex: "output.png")
    """
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    if n == 0 or m == 0:
        print("Grid vazio, não é possível visualizar")
        return
    
    # Cria a figura
    fig, ax = plt.subplots(figsize=(max(8, m), max(6, n)))
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlim(0, m)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.invert_yaxis()  # Inverte o eixo Y para que (0,0) fique no canto superior esquerdo
    
    # Remove os eixos
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Obtém o mapa de cores
    color_map = get_color_map()
    
    # Desenha cada célula
    for i in range(n):
        for j in range(m):
            value = grid[i][j]
            color = color_map.get(value, 'white')
            
            # Desenha o retângulo
            rect = Rectangle((j, i), 1, 1, 
                           facecolor=color, 
                           edgecolor='gray', 
                           linewidth=0.5)
            ax.add_patch(rect)
            
            # Adiciona o valor numérico no centro da célula
            text_color = 'white' if value == 1 else 'black'
            ax.text(j + 0.5, i + 0.5, str(value), 
                   ha='center', va='center', 
                   fontsize=10, fontweight='bold',
                   color=text_color)
    
    # Adiciona grade
    for i in range(n + 1):
        ax.axhline(i, color='gray', linewidth=0.5)
    for j in range(m + 1):
        ax.axvline(j, color='gray', linewidth=0.5)
    
    plt.tight_layout()
    
    # Salva ou mostra
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Imagem salva em: {save_path}")
    
    plt.show()


def visualize_before_after(grid_before, grid_after, save_path=None):
    """
    Visualiza o grid antes e depois lado a lado.
    
    Args:
        grid_before: Grid antes do preenchimento
        grid_after: Grid depois do preenchimento
        save_path: Caminho opcional para salvar a imagem
    """
    n = len(grid_before)
    m = len(grid_before[0]) if n > 0 else 0
    
    if n == 0 or m == 0:
        print("Grid vazio, não é possível visualizar")
        return
    
    # Cria a figura com dois subplots lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(max(16, m * 2), max(6, n)))
    fig.suptitle('Grid: Antes e Depois do Flood Fill', fontsize=16, fontweight='bold')
    
    # Obtém o mapa de cores
    color_map = get_color_map()
    
    # Função auxiliar para desenhar um grid
    def draw_grid(ax, grid, title):
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlim(0, m)
        ax.set_ylim(0, n)
        ax.set_aspect('equal')
        ax.invert_yaxis()
        ax.set_xticks([])
        ax.set_yticks([])
        
        for i in range(n):
            for j in range(m):
                value = grid[i][j]
                color = color_map.get(value, 'white')
                
                rect = Rectangle((j, i), 1, 1, 
                               facecolor=color, 
                               edgecolor='gray', 
                               linewidth=0.5)
                ax.add_patch(rect)
                
                text_color = 'white' if value == 1 else 'black'
                ax.text(j + 0.5, i + 0.5, str(value), 
                       ha='center', va='center', 
                       fontsize=10, fontweight='bold',
                       color=text_color)
        
        # Adiciona grade
        for i in range(n + 1):
            ax.axhline(i, color='gray', linewidth=0.5)
        for j in range(m + 1):
            ax.axvline(j, color='gray', linewidth=0.5)
    
    # Desenha ambos os grids
    draw_grid(ax1, grid_before, "Antes")
    draw_grid(ax2, grid_after, "Depois")
    
    plt.tight_layout()
    
    # Salva ou mostra
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Imagem salva em: {save_path}")
    
    plt.show()

