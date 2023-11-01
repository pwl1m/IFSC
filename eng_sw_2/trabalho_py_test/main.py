from usuario import Funcionario, Jogador

def main():
    sair = False  #controle para sair do loop
    usuario = None  #armazenar o usuário (jogador ou funcionário)

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
            if isinstance(usuario, Jogador): #teste de tipo (type test)
                carteira_cliente = usuario.carteira
                print("Saldo atual:", carteira_cliente.consultar_saldo())

                valor_operacao = float(input("Digite o valor da operação: "))
                tipo_operacao = input("Tipo de operação (adicionar/sacar): ").lower()

                if tipo_operacao == "adicionar":
                    carteira_cliente.adicionar_saldo(valor_operacao)
                elif tipo_operacao == "sacar":
                    sucesso = carteira_cliente.sacar(valor_operacao)
                    if sucesso:
                        print("Saque bem-sucedido.")
                else:
                    print("Operação inválida.") # remover para teste

                print("Saldo após a operação:", carteira_cliente.consultar_saldo(),"\n")

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
