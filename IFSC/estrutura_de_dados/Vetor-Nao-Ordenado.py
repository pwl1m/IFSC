import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__ultimo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)
# caso o ultimo indice usado seja diferente de -1
# O loop começa com i valendo zero e vai até o último elemento, que é indicado pelo valor self.__ultimo. Como o vetor começa com o índice zero, o último elemento do vetor é self.__ultimo - 1.
    def imprime(self):
        if self.__ultimo == -1:
            print("vetor vazio")
        else:
            for i in range(self.__ultimo + 1):
                print(f"{i} - {self.__valores[i]}")

    def insere(self, valor):
        if self.__ultimo == self.__capacidade - 1: # verifica se o vetor ja ta cheio
            print("capacidade maxima atingida")
        else:
            self.__ultimo += 1 # se ainda houver espaco para inseir u novo valor é incrementado o indice da ultima posicao do vetor com += 1
            self.__valores[self.__ultimo] = valor #atualizando a posicao no final do vetor

    def pesquisa(self, valor): # pesquisa a ultima posicao
        for i in range(self.__ultimo + 1):
            if valor == self.__valores[i]:
             print(f'O valor {valor} foi encontrado na posição {i}')
        return -1

    def exclude(self, valor):
        posicao = self.pesquisa(valor)
        if posicao != -1:
            for i in range(posicao, self.__ultimo - 1):
                self.__valores[i] = self.__valores[i + 1] # percorre o vetor da posição do valor encontrado até o último elemento, movendo cada elemento uma posição para trás para preencher o espaço deixado pelo valor excluído.
            self.__ultimo -= 1 #  indicar que o último elemento do vetor foi reduzido em 1, para que a próxima inserção possa ser feita corretamente

v = VetorNaoOrdenado(10)
v.imprime()
v.insere(0)
v.insere(1)
v.insere(2)
v.insere(3)
v.insere(4)
v.imprime()
v.pesquisa(99)
v.pesquisa(2)
v.imprime()
v.exclude(3)
v.imprime()
