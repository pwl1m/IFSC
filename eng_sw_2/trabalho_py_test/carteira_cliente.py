class CarteiraCliente:
    def __init__(self, numero_carteira, saldo):
        self.numero_carteira = numero_carteira
        self.saldo = saldo

    def adicionar_saldo(self, valor):
        self.saldo += valor

    def sacar(self, valor_saque):
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def consultar_saldo(self):
        return self.saldo
