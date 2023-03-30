# import numpy as np
# class pilha:

#     def __init__(self, capacidade):
#         self.__capacidade = capacidade
#         self.__topo = -1
#         self.__valores = np.empty(self.__capacidade, dtype=int)

#     def pilha_cheia(self):
#      if self.__topo == self.__capacidade -1:
#       return True
#      return False

#     def pilha_vazia(self):
#      if self.__topo == -1:
#       return True
#      return False

#     def empilhar(self):
#      if self.__pilha_cheia() == True:
#         print('pilha ta cheia')
#         return
#      self.__topo += 1
#      self.__valores[self.__topo] = valor
#      print('valor adicionado na pilha')
#      return self.__valores[self.__topo]

#     def desempilhar(self):
#         if self.pilha_vazia() == True:
#             print('pilha vazia')
#         removido=self.__valores[self.__topo]
#         self.__valores = np_delete (self.__valores)
#         self.__topo -=1
#         return removido

#     def vertopo(self):
#      if self.pilha_vazia() == True:
#         print ('pilha vazia')
#         return
#      print (f'valor no topo {self.__valores}')
#      return self.__valores[self.__topo]

import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def pilha_cheia(self):
        return self.__topo == self.__capacidade - 1

    def pilha_vazia(self):
        return self.__topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print('pilha ta cheia')
            return
        self.__topo += 1
        self.__valores[self.__topo] = valor
        print('valor adicionado na pilha')

    def desempilhar(self):
        if self.pilha_vazia():
            print('pilha vazia')
            return
        removido = self.__valores[self.__topo]
        self.__valores[self.__topo] = 0  # Set removed value to 0
        self.__topo -= 1
        return removido

    def vertopo(self):
        if self.pilha_vazia():
            print('pilha vazia')
            return
        print(f'valor no topo {self.__valores[self.__topo]}')
        return self.__valores[self.__topo]


v=Pilha(5)
v.empilhar(1)
v.empilhar(2)
v.empilhar(3)
v.empilhar(4)
v.vertopo()
v.desempilhar()
v.vertopo()