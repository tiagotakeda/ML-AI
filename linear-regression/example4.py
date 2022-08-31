import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import plotly.express as px
import plotly.graph_objects as go
from createGrid import createGrid


# Para efeito de contextualização, suponha que uma transportadora
# observou uma correlação entre o tempo de entrega da mercadoria
# com o número de pacotes a serem entregues:

data = {
    'n': [20, 12, 11, 3, 19, 9, 19, 17, 7, 7, 8, 11, 12, 19, 2, 7, 6, 10, 10, 7, ],
    't': [92.0, 78.25, 65.75, 62.0, 102.0, 78.0, 118.5, 102.0, 68.0, 68.0, 62.0, 80.0, 70.5, 82.75, 96, 74.5, 80.5, 61.75, 93.75, 37.0],
    'd': [188, 197, 119, 140, 236, 184, 290, 284, 168, 128, 104, 220, 118, 191, 168, 226, 226, 111, 295, 72]
}


def regressaoSimples():
    data = {
        'n': [20, 12, 11, 3, 19, 9, 19, 17, 7, 7, 8, 11, 12, 19, 2, 7, 6, 10, 10, 7, ],
        't': [92.0, 78.25, 65.75, 62.0, 102.0, 78.0, 118.5, 102.0, 68.0, 68.0, 62.0, 80.0, 70.5, 82.75, 96, 74.5, 80.5, 61.75, 93.75, 37.0],
    }

    # Título do gráfico
    plt.title(
        'Tempo de entrega em função da quantidade de pacotes a serem entregues')
    # Legenda do eixo x
    plt.xlabel('Tempo (minutos)')
    # Legenda do eixo y
    plt.ylabel('Número de Pacotes (inteiros)')

    x = np.array(data['n'])
    y = np.array(data['t'])

    # alpha = (x.size * np.sum(x*y) - np.sum(x) * np.sum(y)) / \
    #     (x.size * np.sum(x*x) - (np.sum(x))**2)

    # beta = np.average(y) - alpha * np.average(x)

    coefs0, res0, _, _, _ = np.polyfit(x=x, y=y, deg=1, full=True)

    a0, b0 = coefs0

    def L0(x): return a0*x + b0
    # def L1(x): return alpha*x + beta

    plt.scatter(data['n'], data['t'], color='blue')
    plt.plot(x, L0(x), color='red')

    plt.show()


# A mesma empresa correlacionou os dados acima só que agora junto com as distâncias
# percorridas em cada uma das entregas:


def regressaoMultipla():
    data = {
        'n': [20, 12, 11, 3, 19, 9, 19, 17, 7, 7, 8, 11, 12, 19, 2, 7, 6, 10, 10, 7, ],
        't': [92.0, 78.25, 65.75, 62.0, 102.0, 78.0, 118.5, 102.0, 68.0, 68.0, 62.0, 80.0, 70.5, 82.75, 96, 74.5, 80.5, 61.75, 93.75, 37.0],
        'd': [188, 197, 119, 140, 236, 184, 290, 284, 168, 128, 104, 220, 118, 191, 168, 226, 226, 111, 295, 72]
    }

    df2 = pd.DataFrame(data)
    # print('df2.head(): \n', df2.head())

    # Seleciona todas as linhas das colunas 'n' e 't'
    indep_plano = df2.loc[:, ['n', 'd']]
    # print('indep_plano.head(): \n', indep_plano.head())

    # Adiciona uma coluna 'const' à direita do DataFrame original
    indep_plano = sm.add_constant(indep_plano, prepend=False)
    # print('indep_plano.head(): \n', indep_plano.head())

    dep_plano = df2['t']  # Variável dependente

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
    def h(n, d): return a_plano*n + b_plano*d + c_plano

    # print('10 pacotes entregues em 200km: ', h(20, 830), ' min')

    # Obtém os dados necessários para desenhar o plano
    x_plano, y_plano, z_plano = createGrid(h, df2['n'], df2['d'], 20)

    # Plota o plano (superfície)
    fig = go.Figure(data=[go.Surface(
        z=z_plano, x=x_plano, y=y_plano,
        colorbar=dict(title='Profundidade'),
        colorscale='Viridis',
        opacity=0.8
    )])

    # Adiciona os pontos (gráfico de dispersão)
    fig.add_scatter3d(
        x=df2['n'], y=df2['d'], z=df2['t'],
        marker=dict(size=6.5, color='crimson'),
        mode="markers",
    )

    # Customizações do gráfico
    fig.update_layout(
        title='Tempo e distâncias percorridas pelo número de pacotes',
        width=600, height=600,
        margin=dict(l=40, r=40, b=40, t=40),
        scene=dict(
            xaxis_title='Número de Pacotes (inteiro)',
            yaxis_title='Distância (Km)',
            zaxis_title='Tempo (Min)'
        )
    )

    # fig.show()

    # fig = px.scatter_3d(data, x='n', y='t', z='d', color='d')

    # # Customizações do gráfico
    # fig.layout.coloraxis.colorbar.title = 'Distância Percorrida'
    # fig.update_layout(
    #     title='Tempo e distâncias percorridas pelo número de pacotes',
    #     width=600, height=600,
    #     margin=dict(l=40, r=40, b=40, t=40),
    #     scene=dict(
    #         xaxis_title='Número de Pacotes (inteiro)',
    #         yaxis_title='Tempo (Min)',
    #         zaxis_title='Distância (Km)'
    #     ),
    # )

    # fig.show()


regressaoMultipla()
