# Algoritmo Flood Fill - Trabalho FPAA

## Descrição do Problema

Este projeto implementa o algoritmo **Flood Fill** para preenchimento de regiões em um grid 2D, simulando um cenário onde um robô precisa mapear um terreno com obstáculos.

### Contexto

Imagine um robô explorador que precisa mapear um terreno representado por uma matriz bidimensional. O terreno possui:
- **Áreas navegáveis** (valor 0): locais onde o robô pode se mover
- **Obstáculos** (valor 1): paredes ou barreiras que o robô não pode atravessar
- **Regiões já mapeadas** (valores 2, 3, 4, ...): áreas que já foram identificadas e coloridas

O objetivo é usar o algoritmo Flood Fill para:
1. Identificar todas as regiões conectadas de células navegáveis
2. Colorir cada região com uma cor diferente
3. Visualizar o resultado tanto em formato texto quanto gráfico

## Explicação do Algoritmo Flood Fill

O **Flood Fill** é um algoritmo clássico usado para preencher uma região conectada em uma estrutura de dados bidimensional. É similar à ferramenta "balde de tinta" em programas de edição de imagem.

### Como Funciona

A implementação utiliza **DFS (Depth-First Search)** com uma pilha:

1. **Inicialização**: Começa em uma célula inicial (x, y) que deve ter valor 0 (navegável)
2. **Preenchimento**: Marca a célula atual com a cor desejada
3. **Exploração**: Verifica os 4 vizinhos ortogonais (cima, baixo, esquerda, direita)
4. **Recursão**: Para cada vizinho que também é navegável (valor 0), repete o processo
5. **Parada**: O algoritmo para quando não há mais células navegáveis conectadas

### Características da Implementação

- **Não atravessa obstáculos**: Células com valor 1 são ignoradas
- **Respeita regiões já coloridas**: Células com valor >= 2 não são modificadas
- **Preenchimento automático**: Após preencher uma região, procura automaticamente por outras regiões não preenchidas
- **Cores sequenciais**: Cada nova região recebe uma cor incremental (2, 3, 4, 5, ...)

### Complexidade

- **Tempo**: O(n × m) onde n e m são as dimensões do grid
- **Espaço**: O(n × m) no pior caso (quando toda a matriz é uma única região)

## Como Configurar e Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passo a Passo

#### 1. Criar Ambiente Virtual (Recomendado)

```bash
# No Windows
python -m venv venv

# Ativar o ambiente virtual
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- `matplotlib`: Para visualização gráfica dos grids

#### 3. Executar o Programa

```bash
# A partir da raiz do projeto
python src/main.py
```

Ou, se estiver dentro da pasta `src`:

```bash
python main.py
```

### Estrutura do Projeto

```
Trabalho-em-grupo-2-FPAA/
├── src/
│   ├── __init__.py          # Módulo principal
│   ├── main.py              # Ponto de entrada do programa
│   ├── flood_fill.py        # Implementação do algoritmo Flood Fill
│   ├── grid_utils.py        # Utilitários para manipulação do grid
│   └── visualization.py     # Visualização texto e gráfica
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## Exemplos de Uso

### Exemplo 1

**Grid de entrada:**
```
0 0 0 1 0
0 1 0 1 0
0 0 0 0 0
1 1 1 0 0
0 0 0 0 1
```

**Coordenadas iniciais:** (0, 0)

**Grid de saída:**
```
2 2 2 1 3
2 1 2 1 3
2 2 2 2 3
1 1 1 2 3
4 4 4 4 1
```

**Explicação:**
- A região conectada começando em (0,0) foi preenchida com cor 2
- A região isolada no canto superior direito foi preenchida com cor 3
- A região isolada no canto inferior esquerdo foi preenchida com cor 4

### Exemplo 2

**Grid de entrada:**
```
0 0 1 0 0 0
0 1 1 0 1 0
0 0 0 0 1 0
1 1 0 1 1 0
0 0 0 0 0 0
```

**Coordenadas iniciais:** (0, 0)

**Grid de saída:**
```
2 2 1 3 3 3
2 1 1 3 1 3
2 2 2 2 1 3
1 1 2 1 1 3
4 4 4 4 4 3
```

**Explicação:**
- A região grande conectada foi dividida em várias sub-regiões devido aos obstáculos
- Cada região isolada recebeu uma cor diferente

### Visualização Gráfica

O programa também gera visualizações gráficas usando matplotlib:

- **0 (navegável)**: Branco
- **1 (obstáculo)**: Preto
- **2 (região 1)**: Vermelho
- **3 (região 2)**: Laranja
- **4 (região 3)**: Amarelo
- **5 (região 4)**: Verde
- **6 (região 5)**: Ciano
- **7 (região 6)**: Azul
- **8 (região 7)**: Roxo
- E assim por diante...

As imagens são salvas automaticamente como:
- `exemplo1_resultado.png`
- `exemplo2_resultado.png`
- `exemplo_customizado_resultado.png`

## Funcionalidades Implementadas

### Módulos Principais

1. **`flood_fill.py`**
   - `flood_fill(grid, x, y, color)`: Preenche uma região conectada
   - `fill_all_regions(grid, start_x, start_y)`: Preenche todas as regiões automaticamente

2. **`grid_utils.py`**
   - `create_empty_grid(n, m)`: Cria um grid vazio
   - `copy_grid(grid)`: Cria cópia do grid
   - `validate_grid(grid)`: Valida formato do grid

3. **`visualization.py`**
   - `print_grid_text(grid, title)`: Imprime grid no terminal
   - `visualize_grid_graphic(grid, title, save_path)`: Visualização gráfica
   - `visualize_before_after(grid_before, grid_after, save_path)`: Comparação antes/depois

4. **`main.py`**
   - Função principal que executa os exemplos
   - Demonstra o uso de todas as funcionalidades

## Notas Técnicas

### Representação do Grid

O grid é representado como uma **lista de listas** em Python:
- `grid[i][j]` representa a célula na linha `i` e coluna `j`
- Valores válidos: 0 (navegável), 1 (obstáculo), 2+ (regiões coloridas)

### Coordenadas

- **x (linha)**: Índice da linha, começando em 0 no topo
- **y (coluna)**: Índice da coluna, começando em 0 à esquerda
- Exemplo: `grid[0][0]` é o canto superior esquerdo

### Algoritmo de Preenchimento

A implementação usa **DFS iterativo com pilha** ao invés de recursão para evitar problemas com grids muito grandes (stack overflow). A pilha armazena as coordenadas (x, y) das células a serem processadas.

## Aplicações do Flood Fill

O algoritmo Flood Fill tem diversas aplicações práticas:

- **Edição de imagens**: Ferramenta "balde de tinta" em editores gráficos
- **Jogos**: Detecção de áreas conectadas, pathfinding
- **Processamento de imagens**: Segmentação de regiões
- **Robótica**: Mapeamento de ambientes, navegação
- **Análise de dados**: Identificação de clusters em matrizes

## Autores

Projeto desenvolvido para a disciplina **Fundamentos de Projeto e Análise de Algoritmos (FPAA)**.

