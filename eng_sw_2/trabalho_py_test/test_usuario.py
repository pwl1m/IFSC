import pytest
from usuario import Usuario, Jogador

# O PARÂMETRO "USUARIO" É UMA FIXTURE, QUE É UM OBJETO QUE PODE SER USADO EM VÁRIOS TESTES
# A FIXTURE É CRIADA COMO DECORATOR DO _> PYTEST.FIXTURE
# O NOME DA FIXTURE É O NOME DO PARÂMETRO DA FUNÇÃO DE TESTE
# PODEM SER USADA EM VÁRIOS TESTES SENDO CRIADAS EM UM ARQUIVO E BASTA IMPORTALA
@pytest.fixture
def user():
    return Usuario(1, "Alice")

@pytest.fixture
def player():
    return Jogador(3, "Charlie")

# TESTE DE INICIALIZAÇÃO DO USUÁRIO
def test_inicializacao_usuario(user: Usuario):
    assert user.id == 1
    assert user.nome == "Alice"

# TESTE DE INICIALIZAÇÃO DO JOGADOR
def test_inicializacao_jogador(player: Jogador):
    assert player.id == 3
    assert player.nome == "Charlie"
    assert player.carteira.numero_carteira == "12345"
    assert player.carteira.saldo == 100.0
    
# TESTE DE CONSULTA DE SALDO NA CARTEIRA DO JOGADOR
def test_consultar_saldo_jogador(player: Jogador):
    saldo = player.carteira.consultar_saldo()
    assert saldo == 100.0

# ADICAO DE SADO NA CARTEIRA DO JOGADOR
def test_adicionar_saldo_jogador(player: Jogador):
    player.carteira.adicionar_saldo(50)
    assert player.carteira.saldo == 150.0

# TESTE DE SAQUE NA CARTEIRA DO JOGADOR
def test_sacar_saldo_jogador(player: Jogador):
    resultado = player.carteira.sacar(50)
    assert resultado == True
    assert player.carteira.saldo == 50.0

if __name__ == "__main__":
    pytest.main()