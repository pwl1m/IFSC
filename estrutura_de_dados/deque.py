import numpy as np

class Deque:

    def _init_(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.fim = 0
        self.numero_elementos = 0
        self.valores = np.empty (self.capacidade, dtype=int)
# verifica se o inicio ta na posicao 0 e o ultimo inserido é o tamanho da capacidade -1
# e se o final + 1 é igual ao inicial
    def deque_cheio(self):
        return (self.inicio == 0 and self.fim == self.capacidade -1) or (self.fim + 1 == self.inicio)
# verificar se esta vazio mas e se ele ficar vazio em outra posicao
    def deque_vazio(self):
        return self.inicio == -1

    def add_inicio(self,valor):
        if self.deque_cheio == -1:
            print('O deque esta cheio')
            return
#se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
# inicio estiver na primeira posicao
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor
        self.quantidade += 1

    def add_fim(self.valor):
        if self.deque_cheio == -1:
            print('O deque esta cheio')
            return
#

    def verinicio(self):
        print(f'')

    def verfim(self):

        

x = Deque(8)
x.insere_inicio(2)
x.insere_inicio(4)
x.insere_inicio(5)
x.insere_inicio(7)
