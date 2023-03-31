import numpy as np

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.valor = np.empty(self.capacidade, dtype=int)
        self.maxfila = 10

    def filacheia(self):
        return self.fim == self.capacidade-1

    def filavazia(self):
        return self.fim == -1

    def entrafila (self,unidade):
        if self.filacheia():
            print('FILA CHEIA')
            return
        self.fim += 1
        self.valor[self.fim] = unidade
        print('VALOR ADICIONADO')

   # def saidafila (self):
    def ultfila(self):
        if self.filavazia():
            print('VAZIA')
            return
        print(f'PRIMEIRO DA FILA {self.valor[0]}')
        return self.valor[self.fim]

x=fila(4)
x.entrafila(1)
x.entrafila(1)
x.entrafila(1)
x.entrafila(100)
x.ultfila()