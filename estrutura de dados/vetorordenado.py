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
                print(f"[{i}] - {self.__valores[i]} |", end=" ")

    def insere(self, valor):
        # verificar se o vetor esta cheio
        if self.__ultimo == self.__capacidade - 1:
            print("capacidade maxima atingida", end=" ")
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
                print(f"[{i}] - Encontrado |", end=" ")
                return i
            else:
                 print(f"[{i}] - Nao Encontrado |", end=" ")

    def SearxBin(self, valor): # pesquisa binaria
        min=0
        max=self.__ultimo
        while True:
            pos = int ((min+max) / 2)
            if self.__valores[pos] == valor:
                print ("posicao dos valores igual ao valor")
                return pos
            elif min > max:
                print ("elif min > max")
                return -1
            else:
                if self.__valores[pos] < valor:
                    min = pos + 1
                    print("Menor que o valor")
                else: 
                    max = pos - 1
                    print("maior que o valor")

    def imprime_array(self):
        print(self.__valores[:self.__ultimo + 1])

    def umespaco(self):
        print("\n")

v = VetorOrdenado(12)
v.insere(99)
v.insere(137)
v.insere(27)
v.insere(55)
v.insere(50)
v.insere(88)
v.insere(277)
v.insere(33)
v.insere(28)
v.insere(30)
v.insere(66)
v.insere(44)
v.imprime_array()
v.SearxBin(137)
v.pesquisa(88)
v.umespaco()
v.imprime()