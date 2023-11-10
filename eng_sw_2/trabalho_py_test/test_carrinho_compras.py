# test_carrinho_compras.py
import pytest
from carrinho_compras import CarrinhoDeCompras
from carteira_cliente import CarteiraCliente

@pytest.fixture
def carteira_cliente():
    return CarteiraCliente("12345", 200.0)

def test_adicionar_compra(carteira_cliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    carrinho.adicionar_compra('major')
    assert carrinho.compras == ['mini', 'major']

def test_calcular_total(carteira_cliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    carrinho.adicionar_compra('major')
    total = carrinho.calcular_total()
    assert total == 60

# def test_realizar_compra_saldo_insuficiente(carteira_cliente):
#     carrinho = CarrinhoDeCompras(carteira_cliente)
#     carrinho.adicionar_compra('mega')
#     saldo_anterior = carteira_cliente.consultar_saldo()
#     resultado = carrinho.realizar_compra()
#     assert resultado is False
#     assert carteira_cliente.consultar_saldo() == saldo_anterior  # O saldo não deve ser alterado

def test_realizar_compra_saldo_suficiente(carteira_cliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    saldo_anterior = carteira_cliente.consultar_saldo()
    resultado = carrinho.realizar_compra()
    assert resultado is not False
    assert carteira_cliente.consultar_saldo() == saldo_anterior - 10  # O saldo deve ser reduzido

def test_total_compras(carteira_cliente):
    carrinho = CarrinhoDeCompras(carteira_cliente)
    carrinho.adicionar_compra('mini')
    carrinho.adicionar_compra('major')
    carrinho.realizar_compra()
    assert carrinho.total_compras == 60
