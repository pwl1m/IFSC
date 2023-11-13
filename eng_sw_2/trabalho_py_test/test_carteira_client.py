import pytest
from carteira_cliente import CarteiraCliente 

# Teste de inicialização da carteira
@pytest.fixture
def carteira():
    return CarteiraCliente("12345", 100)
    
def test_inicializacao_carteira(carteira: CarteiraCliente):
    assert carteira.numero_carteira == "12345"
    assert carteira.saldo == 100

# ADICAO DE SALDO
def test_adicionar_saldo(carteira: CarteiraCliente):
    saldo_anterior = carteira.consultar_saldo()
    carteira.adicionar_saldo(50)
    saldo_atual = carteira.consultar_saldo()
    # ASSERT - VERIFICA SE O RESULTADO ESPERADO É IGUAL AO RESULTADO OBTIDO
    assert saldo_atual == saldo_anterior + 50
    
# Teste de exceção
# def test_adicionar_saldo_invalido(carteira: CarteiraCliente):
#     with pytest.raises(Exception) as assert_error:
#         carteira.adicionar_saldo(-50)
#     assert str(assert_error.value) == "Valor inválido."

# SAQUE
def test_sacar_saldo_suficiente(carteira: CarteiraCliente):
    resultado = carteira.sacar(50)
    assert resultado == True
    assert carteira.saldo == 50

# SACAR A MAIS
def test_sacar_saldo_insuficiente(carteira: CarteiraCliente):
    resultado = carteira.sacar(150)
    assert resultado == False
    assert carteira.saldo == 100  # O saldo não deve mudar

# CONSULTA SALDO
def test_consultar_saldo(carteira: CarteiraCliente):
    saldo = carteira.consultar_saldo()
    assert saldo == 100

# COMBINANDO OPERAÇÕES DE ADICAO E SAQUE 
def test_operacoes_combinadas(carteira: CarteiraCliente):
    carteira.adicionar_saldo(50)
    resultado = carteira.sacar(75)
    assert resultado == True
    assert carteira.saldo == 75

# COMBINADO ADICAO / SAQUE E SALDO INSUFICIENTE
def test_operacoes_combinadas_saldo_insuficiente(carteira: CarteiraCliente):
    carteira.adicionar_saldo(50)
    resultado = carteira.sacar(175)
    assert resultado == False
    assert carteira.saldo == 150
        

# # teste de valor positivo
# def test_check_number_positive(carteira: CarteiraCliente):
#     with pytest.raises(Exception) as assert_error:
#         carteira.check_positive_number(-50)
#     assert str(assert_error.value) == "Valor inválido."

# #Teste_de adição de saldo inválido
# def test_adicionar_saldo_invalido(carteira: CarteiraCliente):
#     with pytest.raises(Exception, match="Não é possível adicionar um valor negativo."):
#         carteira.adicionar_saldo(-50)
#     assert carteira.consultar_saldo() == 100