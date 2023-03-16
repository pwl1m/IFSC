# array tem capacidade de conter apenas elementos homogeneos
# usando a classe array do python
import numpy as np

class VetorNaoOrdenado: 
 def __init__ (self, capacidade):
  self.__capacidade = capacidade
  self.__ultimo = -1 
  self.__valores = np.empty(self.__capacidade, dtype=int) 

 def imprime (self):
  if self.__ultimo == -1:
    print ("vetor vazio")
  else:
    for i in range(self.__ultimo+1):
     print(f'{i} - {self.__valores[i]}')

 def insere(self,valor):
   if self.__ultimo == self.__capacidade -1:
     print('capacidade maxima atingida')
   else:
    self.__ultimo += 1
    self.__valores[self.__ultimo] = valor

def pesquisa(self,valor): 
  for i in range(self.__ultimo):
    if valor == self.__valores[i]:
      return i

def exclude(self,valor):
  # posicao = self.pesquisa(valor)
  # if posicao == -1:
    # return -1
    # else:
      # for i in range (posicao,self.ultima_posicao):
        # self.valores[i=self.valores[i+1]
        # self.ultima_posicao -= 1
    if valor == self.__valores[i]:
      return i-1
    print(f"{i}")

v = VetorNaoOrdenado(10)
v.imprime()
v.insere(4)
v.insere(3)
v.insere(8)
v.insere(9)
v.insere(2)
v.insere(7)
v.insere(1)
v.insere(0)
v.insere(5)
v.insere(10)
v.imprime()
v.pesquisa(7)
v.imprime()
v.exclude()