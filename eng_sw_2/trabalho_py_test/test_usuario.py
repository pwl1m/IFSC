import pytest
from usuario import Usuario, Funcionario, Jogador

# Teste de inicialização do usuário
def test_inicializacao_usuario():
    usuario = Usuario(1, "Alice")
    assert usuario.id == 1
    assert usuario.nome == "Alice"

# Teste de inicialização do funcionário
def test_inicializacao_funcionario():
    funcionario = Funcionario(2, "Bob")
    assert funcionario.id == 2
    assert funcionario.nome == "Bob"

# Teste de inicialização do jogador
def test_inicializacao_jogador():
    jogador = Jogador(3, "Charlie")
    assert jogador.id == 3
    assert jogador.nome == "Charlie"
    assert jogador.carteira.numero_carteira == "12345"
    assert jogador.carteira.saldo == 100.0

# Teste de adição de saldo na carteira do jogador
def test_adicionar_saldo_jogador():
    jogador = Jogador(3, "Charlie")
    jogador.carteira.adicionar_saldo(50)
    assert jogador.carteira.saldo == 150.0

# Teste de saque na carteira do jogador
def test_sacar_saldo_jogador():
    jogador = Jogador(3, "Charlie")
    resultado = jogador.carteira.sacar(50)
    assert resultado == True
    assert jogador.carteira.saldo == 50.0

# Teste de consulta de saldo na carteira do jogador
def test_consultar_saldo_jogador():
    jogador = Jogador(3, "Charlie")
    saldo = jogador.carteira.consultar_saldo()
    assert saldo == 100.0
