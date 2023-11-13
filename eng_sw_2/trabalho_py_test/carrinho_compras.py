# carrinho_compras.py
class CarrinhoDeCompras:
    def __init__(self, carteira_cliente):
        self.opcoes = {'mini': 10, 'major': 50, 'mega': 100}
        self.compras = []
        self.carteira_cliente = carteira_cliente
        self.total_compras = 0  # Adicione esta linha

    def adicionar_compra(self, opcao):
        if opcao in self.opcoes: # opcao in self.opcoes = verifica se a opção está dentro do dicionário 
            self.compras.append(opcao) # append = adicionar no final da lista 
        else:
            print("Opção de compra inválida.")

    def calcular_total(self):
        return sum(self.opcoes[opcao] for opcao in self.compras)

    # método para atualizar o total de compras do carrinho 
    def realizar_compra(self):
        total_compra = self.calcular_total()
        print(f"Total da compra: {total_compra}")

        if total_compra > self.carteira_cliente.consultar_saldo(): # Verifica se o saldo é suficiente
            print("Saldo insuficiente para realizar a compra.")
            return False
        else:
            self.carteira_cliente.sacar(total_compra) # carteira_cliente.sacar = chama o método sacar da classe CarteiraCliente 
            print("Compra realizada com sucesso.")
            saldo_atualizado = self.carteira_cliente.consultar_saldo() # Atualiza o saldo
            print("Saldo atual:", saldo_atualizado)
            # Atualiza o total de compras
            self.total_compras += total_compra

            return saldo_atualizado 
    
    
