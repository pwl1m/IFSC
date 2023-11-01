from carteira_cliente import CarteiraCliente

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario(Usuario):
    def __init__(self, id, nome):
        super().__init__(id, nome) 
        
class Jogador(Usuario):
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self.carteira = CarteiraCliente("12345", 1000.0)

