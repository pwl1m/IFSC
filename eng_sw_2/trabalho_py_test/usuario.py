from carteira_cliente import CarteiraCliente

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

class Funcionario(Usuario):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha) 
        
class Jogador(Usuario):
    def __init__(self, id, nome, senha):
        super().__init__(id, nome, senha)
        self.carteira = CarteiraCliente("12345", 100.0)

