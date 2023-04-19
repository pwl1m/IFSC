#import timeit
# def somatorio(n):
#   soma = 0
#   for i in range(1,n+1):
#     soma+=i
#   return soma

#def soma2(n):
#  return (n * ( n + 1 )) / 2 

# #print(somatorio(10))
# # def soma1(n):
# #   soma=0
# #   for i in range (n+1):
# #       soma+=i
# #   return soma

# def lista (n):
#  lista = []
#  for i in range(0,999):
#   lista.append(n)
#  return lista

# def lista2():
#   return range(1000)

# print(lista2())

# l = lista2()
# for i in 1:
#   print(i)

# tempo_inicial = timeit.default_timer()
# lista(1)
# tempo_final = timeit.default_timer()
# print(f'tempo somatorio: {tempo_final - tempo_inicial}')

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
