def processar_pagamento(carteira, valor, tipo_pagamento):
    if tipo_pagamento == "cartao":
        #pagamento com cartão, se necessário.
        pass
    elif tipo_pagamento == "dinheiro":
        carteira.adicionar_saldo(valor)
    else:
        print("Tipo de pagamento inválido.")
