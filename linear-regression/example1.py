import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

data = {
    'h': [1100, 1250, 1400, 1550, 1700, 1850, 2000, 2150, 2300, 2450,
          2600, 2750, 2900, 3050, 3200, 3350, 3500, 3650, 3800, 3950],
    'T': [4.24, 4.27, 4.20, 4.12, 3.93, 3.81, 3.73, 3.50, 3.75, 3.37,
          3.53, 3.48, 3.31, 3.25, 3.29, 3.12, 3.21, 3.19, 3.11, 2.97]
}

alunos = {
    't': [4, 5, 6, 13, 15],
    'n': [3.5, 3.7, 5.0, 8.5, 9.5]
}

# df = pd.DataFrame(data)  # Transforma o dicionário em um DataFrame
# df.head()                # Visualização das primeiras linhas do DataFrame

# sns.scatterplot(x='h', y='T', data=df)  # Gráfico de dispersão

# Título do gráfico
plt.title('Tempertaura oceânica em função de sua profundidade')
# Legenda do eixo x
plt.xlabel('Profundidade (m)')
# Legenda do eixo y
plt.ylabel('Temperatura (°C)')

x1 = np.arange(-100, 100, 1)
# plt.scatter(data['h'], data['T'])

# x = np.array(data['h'])
# y = np.array(data['T'])
x = np.array(alunos['t'])
y = np.array(alunos['n'])
coefs0, res0, _, _, _ = np.polyfit(x=x, y=y, deg=1, full=True)

a0, b0 = coefs0


def L0(x): return a0*x + b0


plt.scatter(alunos['t'], alunos['n'], color='blue')
plt.plot(x, L0(x), color='red')

plt.show()

# plt.plot(x1, x1**2)
# plt.show()
