#criar uma lista de 1000 elementos (0 a 999)
#medir o tempo de criacao da lista 

def lista1():
    lista=[]
    for i in range (1000):
        lista += [i]
    return lista
print(lista1())

def lista2():
    return range(1000)

print (lista2())

l=lista2()
for i in 1:
    print(i)