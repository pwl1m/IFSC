import numpy as np

class filacircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.valor = np.empty(self.capacidade, dtype=int)
        self.n_elementos = 0 # quantidade de elementos

    def filacheia(self):
        return self.n_elementos == self.capacidade

    def filavazia(self):
        return self.n_elementos == 0

    def entrafila(self, unidade):
        if self.filacheia():
            print('if self.filacheia()')
            return
        self.fim = (self.fim + 1) % self.capacidade
        self.valor[self.fim] = unidade
        self.n_elementos += 1
        print(f'{unidade} unidade - entrafila')

    def ultfila(self):
        if self.filavazia():
            print('fila vazia FROM ultfila')
            return
        print(f'ultfila - self.valor[self.fim]: {self.valor[self.fim]}')

    def imprimefila(self):
        if self.filavazia():
            print('if self.filaVazia FROM imprimeFila')
            return
        print('for i in range > self.n_elementos > i+1 - self.valor [self.inicio+i] % .self.capacidade')
        for i in range(self.n_elementos):
            print(f'{i+1}. {self.valor[(self.inicio+i) % self.capacidade]}')

x = filacircular(10)
x.entrafila(0)
x.entrafila(1)
x.entrafila(2)
x.entrafila(3)
x.entrafila(4)
x.entrafila(5)
x.entrafila(6)
x.entrafila(7)
x.entrafila(8)
x.entrafila(9)
x.entrafila(10)
x.ultfila()
x.imprimefila()