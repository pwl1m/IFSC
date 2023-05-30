# def mergesort(lista):
    #precisamos dividir essa lista em outras listas menores(sub-listas), sem criar novas listas, guardando as posicoes de inicio, de fim e de meio, a metade do lado esquerdo inicia na ponta esquerda e vai do inicio ao meio.
    # ja a lista do lado direito, tambem inicia do lado esquerdo(partinda do meio) e vai até o fim da lista(ainda estamos falando da lista da direita)
    # entao dai seriam 3 variaveis de indices (lista, inicio, fim)
    
def mergesort (lista,inicio,fim):
    # if(fim - )
    # verificar se o fim - inciio é maior que 1, porque se maior do que 1 o merge_srte dizer que 
    if(fim-inicio > 1):
        meio = (fim + inicio) // 2  # // para divisão de inteiro
        # 
        mergesort (lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista,inicio,meio,fim)
# etapa de juntar
def merge(lista, inicio, meio, fim):
    # criando a lista da esquerda, o que tiver na lista original des de o inicio ate=":" o meio
    # chega ate a excluir o elemento que ta no meio
    left = lista[inicio:meio]
    # esse pega do meio ate o fim
    right= lista[meio:fim]

    i, j= 0, 0 # explicação seguinte -+- i é o topo da esquerda, j topo da direita

    for k in range(inicio,fim):

        #aqui vai verificar se quem ta no topo da lista da esqeuda e menor de quem ta na lista da direita, entao entra 2 variaveis para gerencialos
        
        # explica-se o i e j
        
        # dando prioridade pra entrar na lista o numero menor
        # o que tiver o topo da esqeurda(o maior)
        # [1,2]
        # for menor do que oq ta no topo do direita(3,4)
        # (2,4), na posicao k da lista(numero que percorre), vai entrar quem ta no topo da left (o maior da esquerda) 
        
        
        # se nao entra na posicao k da lista quem ta no topo da lista da direita(o maior numero)
        if left[i] < right [j]:
            lista[k] = left [i]
        else:
            lista[k] = right[j]