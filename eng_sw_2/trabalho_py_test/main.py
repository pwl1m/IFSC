# main.py
from usuario import Funcionario, Jogador
# from carteira_cliente import CarteiraCliente
from carrinho_compras import CarrinhoDeCompras

def realizar_compras(carrinho):
    while True:
        opcao_compra = input("Escolha uma opção de compra (mini/major/mega) ou 'sair' para sair: ").lower()

        if opcao_compra == 'sair':
            break
        else:
            carrinho.adicionar_compra(opcao_compra)

        saldo_atualizado = carrinho.realizar_compra()

        if saldo_atualizado is not False:
            print("Saldo após a compra:", saldo_atualizado, "\n")

def main():
    sair = False  # controle para sair do loop
    usuario = None  # armazenar o usuário (jogador ou funcionário)
    total_compras = 0

    while not sair:
        if usuario is None:
            tipo_usuario = input("Digite jogador ou funcionario: ").lower()
            if tipo_usuario == 'jogador' or tipo_usuario == 'j':
                usuario = Jogador(1, "Jogador")
            elif tipo_usuario == 'funcionario' or tipo_usuario == 'f':
                usuario = Funcionario(2, "Funcionario")
            else:
                print("Inválido. Digite 'jogador' ou 'funcionario'.")

        if usuario:
            print(f"Olá, {usuario.nome}!")

            # Verifica se o usuário é um jogador antes de acessar a carteira
            if isinstance(usuario, Jogador):  # teste de tipo (type test)
                carteira_cliente = usuario.carteira
                print("Saldo atual:", carteira_cliente.consultar_saldo())

                opcao_operacao = input("Deseja adicionar ou sacar dinheiro? (adicionar/sacar/n): ").lower()

                if opcao_operacao == 'adicionar':
                    valor_operacao = float(input("Digite o valor a ser adicionado: "))
                    carteira_cliente.adicionar_saldo(valor_operacao)

                elif opcao_operacao == 'sacar':
                    valor_operacao = float(input("Digite o valor a ser sacado: "))
                    sucesso = carteira_cliente.sacar(valor_operacao)
                    if sucesso:
                        print("Saque bem-sucedido.")

                opcao_comprar = input("Gostaria de fazer compras? (s/n): ").lower()

                if opcao_comprar == 's':
                    carrinho = CarrinhoDeCompras(carteira_cliente)
                    realizar_compras(carteira_cliente, carrinho)
                    total_compras += carrinho.total_compras

            opcao = input("-- Qualquer tecla repete a operacao \n'trocar' para trocar de usuario \n'sair' para sair --\n").lower()

            if opcao == 'sair':
                sair = True
                print("\nSaindo do sistema.")
            elif opcao == 'trocar':
                usuario = None
            else:
                print("")

if __name__ == "__main__":
    main()
