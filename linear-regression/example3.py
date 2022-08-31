import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import numpy as np
import pandas as pd
from createGrid import createGrid

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


def main():
    data2 = {
        'S': [34.35, 34.67, 34.80, 34.72, 34.88, 34.98, 35.20, 35.00, 35.10, 35.19,
              35.31, 35.20, 35.05, 34.92, 34.88, 34.85, 34.80, 34.77, 34.62, 34.57],
        'T': [4.24, 4.27, 4.20, 4.12, 3.93, 3.81, 3.73, 3.50, 3.75, 3.37,
              3.53, 3.48, 3.31, 3.25, 3.29, 3.12, 3.21, 3.19, 3.11, 2.97],
        'h': [1100, 1250, 1400, 1550, 1700, 1850, 2000, 2150, 2300, 2450,
              2600, 2750, 2900, 3050, 3200, 3350, 3500, 3650, 3800, 3950],
    }

    df2 = pd.DataFrame(data2)
    # print(df2.head())

    # Seleciona todas as linhas das colunas 'S' e 'T'
    indep_plano = df2.loc[:, ['S', 'T']]
    # print(indep_plano.head())

    # Adiciona uma coluna 'const' à direita do DataFrame original
    indep_plano = sm.add_constant(indep_plano, prepend=False)
    # print(indep_plano.head())

    dep_plano = df2['h']  # Variável dependente

    # Define o modelo de regressão linear
    modelo_plano = sm.OLS(dep_plano, indep_plano, hasconst=True)
    # Ajusta a reta aos dados, retornando diversos resultados
    resultados_plano = modelo_plano.fit()

    # Unpack dos coeficientes do plano
    a_plano, b_plano, c_plano = resultados_plano.params

    # Imprime coeficientes
    print(
        f"Coeficientes do plano:\n\na: {a_plano}\nb: {b_plano}\nc: {c_plano}")

    # Define a equação do plano
    def h(S, T): return a_plano*S + b_plano*T + c_plano

    # Obtém os dados necessários para desenhar o plano
    x_plano, y_plano, z_plano = createGrid(h, df2['S'], df2['T'], 20)

    # Plota o plano (superfície)
    fig = go.Figure(data=[go.Surface(
        z=z_plano, x=x_plano, y=y_plano,
        colorbar=dict(title='Profundidade'),
        colorscale='Viridis',
        opacity=0.8
    )])

    # Adiciona os pontos (gráfico de dispersão)
    fig.add_scatter3d(
        x=df2['S'], y=df2['T'], z=df2['h'],
        marker=dict(size=6.5, color='crimson'),
        mode="markers",
    )

    # Customizações do gráfico
    fig.update_layout(
        title='Salinade e temperatura oceânicas pela profundidade',
        width=600, height=600,
        margin=dict(l=40, r=40, b=40, t=40),
        scene=dict(
            xaxis_title='Salinidade (g/kg)',
            yaxis_title='Temperatura (°C)',
            zaxis_title='Profundidade (m)'
        )
    )

    fig.show()

    # fig = px.scatter_3d(data2, x='S', y='T', z='h', color='h')

    # # Customizações do gráfico
    # fig.layout.coloraxis.colorbar.title = 'Profundidade'
    # fig.update_layout(
    #     title='Salinade e temperatura oceânicas pela profundidade',
    #     width=600, height=600,
    #     margin=dict(l=40, r=40, b=40, t=40),
    #     scene=dict(
    #         xaxis_title='Salinidade (g/kg)',
    #         yaxis_title='Temperatura (°C)',
    #         zaxis_title='Profundidade (m)'
    #     ),
    # )

    # fig.show()


main()
