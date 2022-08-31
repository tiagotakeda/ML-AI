import matplotlib.pyplot as plt
import numpy as np

# Para efeito de contextualização, suponha que em uma classe com
# 5 alunos nós quiséssemos relacionar o tempo de estudo (em horas)
# com a nota deles na prova:

alunos = {
    't': [4, 5, 6, 13, 15, 18, 22],
    'n': [3.5, 3.7, 5.0, 8.5, 9.5, 10, 8]
}

# Título do gráfico
plt.title('Nota da prova em função do tempo de estudo individual')
# Legenda do eixo x
plt.xlabel('Tempo (horas)')
# Legenda do eixo y
plt.ylabel('Nota (absoluto)')

x = np.array(alunos['t'])
y = np.array(alunos['n'])

# alpha = (x.size * np.sum(x*y) - np.sum(x) * np.sum(y)) / \
#     (x.size * np.sum(x*x) - (np.sum(x))**2)

# beta = np.average(y) - alpha * np.average(x)

coefs0, res0, _, _, _ = np.polyfit(x=x, y=y, deg=1, full=True)

a0, b0 = coefs0


def L0(x): return a0*x + b0
# def L1(x): return alpha*x + beta


plt.scatter(alunos['t'], alunos['n'], color='blue')
plt.plot(x, L0(x), color='red')

plt.show()
