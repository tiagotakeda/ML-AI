# Introdução à Técnicas de Machine Learning e IA

### Objetivo

O objetivo final deste material é passar uma visão básica e abrangente sobre as principais técnicas e algoritmos de Machine Learning e Artificial Intelligence.

### Tópicos

Infelizmente, é impossível analisarmos todos os algoritmos destas áreas de uma vez só. Portanto vamos nos ater aos modelos mais conhecidos, são eles:

- Linear Regression
- Decision Tree
- Random Forest
- SVM (Support Vector Machine)
- KNN (K Nearest Neighbor)
- Naive Bayes

#### Regrssão Linear

![Linear Regression](https://miro.medium.com/max/1400/1*JplJixyQxHTRwQvqP7eDrQ.gif)

##### Origem

O termo 'Regressão' surgiu em 1885 com o antropólogo, matemático e estatístico Francis Galton. Ele aplicava estes conceitos no estudo do corpo humano.

![Francis Galton](https://miro.medium.com/max/386/0*2dl-pJMeOc0F-A5R)

Ao estudar as estaturas de pais e filhos, Galton observou que filhos de pais com altura baixa em relação à média tendem a ser mais altos que seus pais, e filhos de pais com estatura alta em relação à média tendem a ser mais baixos que seus pais, ou seja, as alturas dos seres humanos em geral tendem a regredir à média.

Regressão linear é um tipo de algoritmo supervisionado, portanto antes de entender como funciona o algoritmo é importante conhecer o que seria aprendizado supervisionado.

##### Algoritmos Supervisionados

Os *algoritmos supervisionados* podem ser subdivididos em *algoritmos de classificação* e *algoritmos de regressão*.

Em resumo a Regressão Linear se resume em um conjunto de multiplicações de matrizes. A complexidade de multiplicar duas matrizes.

#### decision Tree

Primeiro de tudo, é muito importante conhecer bem o seu modelo. Mas, para isso, nós temos esse post aqui para te ensinar o necessário. Depois que você tiver uma ideia, vamos ver como isso funciona. Já deixo claro que é importante o entendimento de árvores binárias para que a seguinte análise flua com mais facilidade.

Basicamente, uma árvore de decisão faz sua avaliação levando em consideração cada divisão dos dados e vai fazer isso para cada feature em cada nó que não é o nó de uma folha. Isso acontece a medida que os níveis continuam. Supondo uma árvore binária totalmente balanceada, a complexidade será O(log(n)), porque você simplesmente deverá contar quantos níveis tem. Se tivermos 1 nó, com 2 filhos e cada um deles com 2 filhos, teremos que analisar 3 camadas (o que é, aproximadamente, log de 8 na base 2, que é 3).

Porém, se tivermos uma árvore totalmente desbalanceada, com uma concentração única em um lado, teremos que andar N camadas, o que nos deixa com uma complexidade de O(n).

Além disso, outra coisa que deve ser levada em consideração é o fato que nós também temos que calcular uma probabilidade em cada nó para calcular a entropia para fazer o corte. Isso adicionará uma complexidade de O(log(n)), na mesma lígica que usamos anteriormente, por causa da estrutura de árvore binária.

Então vejamos, a complexidade de uma Decision Tree será de O(n * p * d * log(n)), sendo d a profundidade de camadas. Aplicando o que acabamos de descobrir, temos que a complexidade da árvore estará entre algo como O(n * p * log²(n)) e O(n² * p * log(n))

#### Random Forest

Se você não está totalmente familiarizado com esse modelo, sugiro esse nosso post.

Esse algoritmo só está aqui porque ele é basicamente o que fizemos antes… Mas multiplicado pelo número de árvores, já que a Random Forest não passa de um monte de resultados comparados de um monte de Decision Trees. Então, considerando o que foi passado anteriormente, podemos ver que a eficiência desse algoritmo estará entre algo como O(n * p * log²(n) * t) e O(n² * p * log(n) * t).