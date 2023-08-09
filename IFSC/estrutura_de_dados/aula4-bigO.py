import timeit

def somatorio(n):
  soma = 0
  for i in range(1,n+1):
    soma+=i
  return soma

def soma2(n):
 return (n * ( n + 1 )) / 2 

print(somatorio(10))
def soma1(n):
  soma=0
  for i in range (n+1):
      soma+=i
  return soma

def lista (n):
 lista = []
 for i in range(0,999):
  lista.append(n)
 return lista

def lista2():
  return range(1000)
print(lista2())

tempo_inicial = timeit.default_timer()
lista(1)
tempo_final = timeit.default_timer()
print(f'tempo somatorio: {tempo_final - tempo_inicial}')