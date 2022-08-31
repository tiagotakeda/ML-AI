import numpy as np
import pandas as pd


def createGrid(func, x, y, size):
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
