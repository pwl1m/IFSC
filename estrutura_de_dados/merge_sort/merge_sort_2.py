def merge_sort(lista):
    # Imprime a lista original antes de cada chamada recursiva
    print("Lista original:", lista)
    
    # Verifica se a lista possui mais de um elemento
    if len(lista) <= 1:
        return lista
    
    # Calcula o ponto médio da lista
    meio = len(lista) // 2
    
    # Divide a lista em duas partes
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Chamada recursiva para ordenar as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Imprime as duas metades da lista antes da etapa de mesclagem
    print("Mesclando:", esquerda, "com", direita)
    
    # Mescla as duas metades ordenadas
    resultado = []
    i = 0  # Índice para percorrer a metade esquerda
    j = 0  # Índice para percorrer a metade direita
    
    # Enquanto existirem elementos nas duas metades
    while i < len(esquerda) and j < len(direita):
        # Compara os elementos das duas metades
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes da metade esquerda (se houver)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Adiciona os elementos restantes da metade direita (se houver)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    # Imprime a lista resultante após a mesclagem
    print("Resultado da mesclagem:", resultado)
    
    return resultado


# Exemplo de uso
lista = [7, 2, 5, 1, 8, 3]
print("Lista original:", lista)
print("Aplicando merge sort...")
ordenada = merge_sort(lista)
print("Lista ordenada:", ordenada)  

# A função merge_sort recebe uma lista como parâmetro e imprime a lista original antes de cada chamada recursiva.

# Verifica-se se a lista possui apenas um elemento ou nenhum. Se sim, a lista é considerada ordenada e é retornada diretamente.

# Se a lista tiver mais de um elemento, o ponto médio é calculado dividindo o tamanho da lista por 2.

# A lista é dividida em duas metades: a parte esquerda contém os elementos até o ponto médio e a parte direita contém os elementos a partir do ponto médio.

# Chamadas recursivas são feitas para ordenar as duas metades da lista separadamente.

# As duas metades ordenadas são mescladas em uma lista resultado, que armazenará a lista final ordenada.

# A mesclagem é feita comparando-se os elementos das duas metades em ordem crescente. Os elementos menores são adicionados primeiro à lista resultado.

# Se ainda houver elementos restantes na metade esquerda ou direita após a comparação inicial, eles são adicionados à resultado.

# A lista resultado após a mesclagem é impressa.

# A lista final ordenada é retornada.

# No exemplo de uso, uma lista é definida (lista = [7, 2, 5, 1, 8, 3]) e é impressa antes da aplicação do merge sort.

# O merge sort é aplicado à lista.

# A lista ordenada é impressa.