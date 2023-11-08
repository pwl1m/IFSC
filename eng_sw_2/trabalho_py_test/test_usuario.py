import pytest
from usuario import Usuario, Jogador

# O parâmetro "usuario" é uma fixture, que é um objeto que pode ser usado em vários testes
# A fixture é criada como decorator do _> pytest.fixture
# O nome da fixture é o nome do parâmetro da função de teste
# Podem ser usada em vários testes sendo criadas em um arquivo e basta importala

@pytest.fixture
def user():
    return Usuario(1, "Alice")

@pytest.fixture
def player():
    return Jogador(3, "Charlie")

# Teste de inicialização do usuário
def test_inicializacao_usuario(user: Usuario):
    assert user.id == 1
    assert user.nome == "Alice"

# Teste de inicialização do jogador
def test_inicializacao_jogador(player: Jogador):
    assert player.id == 3
    assert player.nome == "Charlie"
    assert player.carteira.numero_carteira == "12345"
    assert player.carteira.saldo == 100.0

# Teste de adição de saldo na carteira do jogador
def test_adicionar_saldo_jogador(player: Jogador):
    player.carteira.adicionar_saldo(50)
    assert player.carteira.saldo == 150.0

# Teste de saque na carteira do jogador
def test_sacar_saldo_jogador(player: Jogador):
    resultado = player.carteira.sacar(50)
    assert resultado == True
    assert player.carteira.saldo == 50.0
    
def test_sacar_saldo_jogador_2(player: Jogador):
    resultado = player.carteira.sacar(60)
    assert resultado == True
    assert player.carteira.saldo == 50.0

# Teste de consulta de saldo na carteira do jogador
def test_consultar_saldo_jogador(player: Jogador):
    saldo = player.carteira.consultar_saldo()
    assert saldo == 100.0

if __name__ == "__main__":
    pytest.main()