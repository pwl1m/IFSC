# def mergesort(lista):
    #precisamos dividir essa lista em outras listas menores(sub-listas), guardando as posicoes de inicio, de fim e de meio, a metade do lado esquerdo inicia na ponta esquerda e vai do inicio ao meio.
    # ja a lista do lado direito, tambem inicia do lado esquerdo(partindp do meio) e vai até o fim da lista
    # entao dai seriam 3 variaveis de indices (lista, inicio, fim)
    
def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    
    if fim - inicio > 1:
        meio = (fim + inicio) // 2  # // para divisão de inteiro
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):  # juntando
    # criando a lista da esquerda
    # o que tiver na lista original do inicio até o meio
    left = lista[inicio:meio]
    right = lista[meio:fim]

    i, j = 0, 0  # i é o topo da esquerda, j topo da direita
    for k in range(inicio, fim):
        # aqui verifica se quem está no topo da lista da esquerda é menor do que quem está na lista da direita
        # dando prioridade para adicionar à lista o número menor
        # se o topo da esquerda (o maior)
        # for menor do que o que está no topo da direita
        # na posição k da lista (número que percorre),
        # adiciona o topo da left (o maior da esquerda)
        # caso contrário, adiciona na posição k da lista o que está no topo da lista da direita (o maior número)
        if i >= len(left):
            lista[k] = right[j]
            j += 1
        elif j >= len(right):
            lista[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1

lista = [7, 2, 5, 1, 8, 3]
mergesort(lista)
print(lista)  # Lista ordenada
