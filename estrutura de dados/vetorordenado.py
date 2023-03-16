import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade, valores=None):
        self.__capacidade = capacidade
        self.__ultimo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

        if valores is not None:
            for valor in valores:
                self.insere(valor)

    def imprime(self):
        if self.__ultimo == -1:
            print("vetor vazio")
        else:
            for i in range(self.__ultimo + 1):
                print(f"{i} - {self.__valores[i]}")

    def insere(self, valor):
        if self.__ultimo == self.__capacidade - 1:
            print("capacidade maxima atingida")
        else:
            self.__ultimo += 1
            posicao = self.__ultimo

            while posicao > 0 and self.__valores[posicao - 1] > valor:
                self.__valores[posicao] = self.__valores[posicao - 1]
                posicao -= 1
            self.__valores[posicao] = valor

    def pesquisa(self, valor):
        for i in range(self.__ultimo + 1):
            if valor == self.__valores[i]:
                print(f"{i}")
                return i
            else:
                print('não encontrado')
# asdasd
    def imprime_array(self):
        print(self.__valores[:self.__ultimo + 1])

v = VetorOrdenado(6)    
v.insere(99)
v.insere(2)
v.insere(1)
v.insere(0)
v.insere(0)
v.insere(0)
v.insere(4)
v.insere(4)
v.insere(1)
v.imprime_array()
v.pesquisa(2)
v.imprime()