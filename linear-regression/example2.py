import matplotlib.pyplot as plt
import numpy as np

# Para efeito de contextualização, suponha que em uma amostragem foram
# coletados dados sobre a temperatura (em °C) de um oceano, consoante a
# profundidade da medição (em metros):

data = {
    'h': [1100, 1250, 1400, 1550, 1700, 1850, 2000, 2150, 2300, 2450,
          2600, 2750, 2900, 3050, 3200, 3350, 3500, 3650, 3800, 3950],
    'T': [4.24, 4.27, 4.20, 4.12, 3.93, 3.81, 3.73, 3.50, 3.75, 3.37,
          3.53, 3.48, 3.31, 3.25, 3.29, 3.12, 3.21, 3.19, 3.11, 2.97]
}

# Título do gráfico
plt.title('Tempertaura oceânica em função de sua profundidade')
# Legenda do eixo x
plt.xlabel('Profundidade (m)')
# Legenda do eixo y
plt.ylabel('Temperatura (°C)')


x = np.array(data['h'])
y = np.array(data['T'])

# alpha = (x.size * np.sum(x*y) - np.sum(x) * np.sum(y)) / \
#     (x.size * np.sum(x*x) - (np.sum(x))**2)

# beta = np.average(y) - alpha * np.average(x)

coefs0, res0, _, _, _ = np.polyfit(x=x, y=y, deg=1, full=True)

a0, b0 = coefs0


def L0(x): return a0*x + b0
# def L1(x): return alpha*x + beta


plt.scatter(data['h'], data['T'], color='blue')
plt.plot(x, L0(x), color='red')

plt.show()
