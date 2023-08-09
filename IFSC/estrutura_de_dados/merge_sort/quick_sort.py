def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        pivo = partition(lista, inicio, fim) #p = pivo
        quicksort(lista, inicio, pivo-1)
        quicksort(lista,p+1,fim)

def partition(lista,inicio,fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio,fim):
        if lista[j] <= pivo:
            lista[j], lista[i]=lista[i], lista[j]
            i = i+1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i #posicao do pivot