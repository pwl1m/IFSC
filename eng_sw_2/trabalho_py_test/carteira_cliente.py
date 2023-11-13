class CarteiraCliente:
    def __init__(self, numero_carteira, saldo):
        self.numero_carteira = numero_carteira
        self.saldo = saldo

    def adicionar_saldo(self, valor):
        if valor < 0:
            print("Não é possível adicionar um valor negativo.")
        else:
            self.saldo += valor

    def sacar(self, valor_saque):
        if valor_saque < 0:
            print ("Não é possível sacar um valor negativo.")
        elif valor_saque <= self.saldo:
            self.saldo -= valor_saque
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def consultar_saldo(self):
        return self.saldo