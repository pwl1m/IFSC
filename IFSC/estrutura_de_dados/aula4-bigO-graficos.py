# ATENÇÃO: Instalar matplot como package

import numpy as np  # Para se trabalhar com computação numérica.
import matplotlib.pyplot as plt  # Para geração de gráficos

n = np.linspace(
    1, 10, 100, 50
)  # Gera 100 números entre 1 e 10 e esses números estarão espaçados igualmente, ou seja, linearmente espaçados

print(n)

# Label contendo as funções do Big(O)
labels = ['Constante', 'Logarítmico', 'Linear', 'quadratica','cubica','exponencial']
# np.ones(n.shape) gera 100 números "1".
# shape serve para mostrar o comprimento das dimensões do array
big_o = [np.ones(n.shape), np.log(n), n, n*n, n*n*n, 2**n] 

# Definindo o gráfico
plt.figure(figsize=(5, 4))  # Define o tamanho da figura
plt.ylim(0, 10)  # Define o limite do y
plt.xlim(1, 10)  # Define o limite do y

# Gerando gráficos
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])  #entender essa linha
plt.legend() 
plt.ylabel('Tempo de execução')
plt.xlabel('n')

# Exibindo
plt.show()
