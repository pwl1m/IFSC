# test_carrinho_compras.py
import pytest
from carrinho_compras import CarrinhoDeCompras
from carteira_cliente import CarteiraCliente

@pytest.fixture
def carteira_cliente():
    return CarteiraCliente("12345", 200.0)

def test_adicionar_compra(carteira_cliente: CarteiraCliente):
    carrinho = CarrinhoDeCompras(carteira_cliente) # Instancia o carrinho de compras
    carrinho.adicionar_compra('mini') # Adiciona uma compra
    carrinho.adicionar_compra('major') # Adiciona outra compra
    assert carrinho.compras == ['mini', 'major'] # Verifica se as compras foram adicionadas

def test_calcular_total(carteira_cliente: CarteiraCliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    carrinho.adicionar_compra('major')
    total = carrinho.calcular_total()
    assert total == 60
    
# VERIFICAR O TOTAL DE COMPRAS PELO CARRINHO 
def test_total_compras(carteira_cliente: CarteiraCliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    carrinho.adicionar_compra('major')
    carrinho.realizar_compra()
    assert carrinho.total_compras == 60

def test_realizar_compra_saldo_suficiente(carteira_cliente: CarteiraCliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    saldo_anterior = carteira_cliente.consultar_saldo() # Salva o saldo anterior
    resultado = carrinho.realizar_compra() # Realiza a compra
    assert resultado is not False # Verifica se a compra foi realizada 
    assert carteira_cliente.consultar_saldo() == saldo_anterior - 10  # O saldo deve ser reduzido

# def test_realizar_compra_saldo_insuficiente(carteira_cliente):
#     carrinho = CarrinhoDeCompras(carteira_cliente)
#     carrinho.adicionar_compra('mega')
#     saldo_anterior = carteira_cliente.consultar_saldo()
#     resultado = carrinho.realizar_compra()
#     assert resultado is False # Verifica se a compra não foi realizada
#     assert carteira_cliente.consultar_saldo() == saldo_anterior  # Saldo não alterado