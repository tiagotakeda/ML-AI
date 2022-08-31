import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Até então vimos as regressões que continham uma única variável independente e,
# embora elas de fato sejam bastantes úteis, não são raros os casos mais
# sofisticados: suponha que, junto com a medição de temperatura, foram feitas
# medições de salinidade desse oceano. Assim, a profundidade deixa de ser a única
# variável influenciando na predição, pois agora temos um dado a mais para
# aprimorar a regressão.

# Então, como lidamos com esse dado extra? Mantendo-nos no escopo das regressões
# lineares, estaremos agora abordando brevemente as regressões lineares múltiplas.
# É importante ressaltar que o desenvolvimento prático é bastante análogo, mas não
# necessariamente teremos a capacidade de visualiação. De forma direta: duas
# variáveis nos permitiam estimar uma reta e agora três nos permitirão estimar um
# plano, porém quatro ou mais darão origem a uma generalização chamada
# "hiperplano", a grosso modo, um lugar geométrico que pode estar além daquilo que
# conseguimos visualizar. Para todos os efeitos, a representação gráfica é uma
# feature não indispensável desse modelo, então é possível fazer a regressão linear
# com quantas variáveis forem necessárias.

# Dando início ao procedimento, atualizaremos nossos dados:


def create_grid(func, x, y, size):
    """
    Gera um espaço bidimensional delimitado pelos valores extremos de 'x' e 'y', 
    ao qual aplica uma função 'func' de duas variáveis para criar um grid de 
    tamanho 'size' x 'size'. 

    Recebe:
      * func (function): função aplicada a cada par ordenado do espaço.
      * x (pd.Series): abscissas aplicáveis à função.
      * y (pd.Series): ordenadas aplicáveis à funcão.
      * size (int): dimensão do grid, maior ou igual a 2.

    Retorna:
      * cordinates (tuple): tupla de três posições que contém a
                            correspondência (x,y,z) para 'func'.
    """

    # Obtém valores extremos
    x_max, x_min = np.max(x), np.min(x)
    y_max, y_min = np.max(y), np.min(y)

    # Cria espaço bidimensional
    x_cord = np.linspace(x_min, x_max, size)
    y_cord = np.linspace(y_min, y_max, size)

    grid = {}
    counter = 0

    # Aplica a função a cada par ordenado do espaço
    for x in x_cord:
        row = []
        for y in y_cord:
            z = func(x, y)
            row.append(z)

        grid[counter] = row
        counter += 1

    z_data = pd.DataFrame(grid)
    z_cord = z_data.values

    cordinates = (x_cord, y_cord, z_cord)

    return cordinates


def main():
    data2 = {
        'S': [34.35, 34.67, 34.80, 34.72, 34.88, 34.98, 35.20, 35.00, 35.10, 35.19,
              35.31, 35.20, 35.05, 34.92, 34.88, 34.85, 34.80, 34.77, 34.62, 34.57],
        'T': [4.24, 4.27, 4.20, 4.12, 3.93, 3.81, 3.73, 3.50, 3.75, 3.37,
              3.53, 3.48, 3.31, 3.25, 3.29, 3.12, 3.21, 3.19, 3.11, 2.97],
        'h': [1100, 1250, 1400, 1550, 1700, 1850, 2000, 2150, 2300, 2450,
              2600, 2750, 2900, 3050, 3200, 3350, 3500, 3650, 3800, 3950],
    }

    fig = px.scatter_3d(data2, x='S', y='T', z='h', color='h')

    # Customizações do gráfico
    fig.layout.coloraxis.colorbar.title = 'Profundidade'
    fig.update_layout(
        title='Salinade e temperatura oceânicas pela profundidade',
        width=600, height=600,
        margin=dict(l=40, r=40, b=40, t=40),
        scene=dict(
            xaxis_title='Salinidade (g/kg)',
            yaxis_title='Temperatura (°C)',
            zaxis_title='Profundidade (m)'
        ),
    )

    fig.show()


main()
