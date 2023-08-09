#1 Calcule a soma de dois n´umeros e armazene o resultado em uma variavel
a=1
b=2
soma=a+b
print(soma)

#2 Verifique se um n´umero ´e par ou ´ımpa
a=1
b=2
if a%2==0:
  print("Par")
else:
  print("Ímpar")

print("------------------")
#3 Utilize uma estrutura de repeticao para imprimir todos osnumeros de 1 a 10.
for a in range(0, 10):
  print(a)

#4 leia duas strings e verifique se são iguais
nome1 = 'ana'
nome2 = 'ana'

nome3='paulo'
nome4='roberto'

if nome1 is nome2:
    print('iguais')
else:
    print('diferentes')

if nome3 is nome4:
    print('iguais')
else:
    print('diferentes')

#5 calcule fatorial de um numero
n = int(input("n fatorial= "))
for i in range(1, n):
  resultado = (i*n)
  n = resultado
print (resultado)

#6 leia uma lista de numeros e imprima o maior numero da lista
listam = [10, 20, 4, 45, 99, 22] 
print("maior", max(listam)) 

# 7
num = int(input("n primo= "))
divisor = 2
while num % divisor != 0:
  divisor += 1
  print(divisor)
  if divisor == num:
    print("nao primo")

#8
soma = 0
cont = 0
for c in range(0,6):
    num=int(input('digite o {} valor:'.format(c)))
    if num % 2 == 0:
        soma+=num
        cont+=1
print('numeros pares {} soma {}'.format(cont,soma))

#9
listam = [10, 20, 4, 45, 99, 22] 
print("menor e maior", min(listam), max(listam)) 

#10
lista1 = ['ana','bia','jacare', 'pedra', 'uranio'] 
lista2 = ['bia','jacare', 'peixe', 'mercurio','ana']

print(set(lista1) & set(lista2))

#11
lista = [10, 20, 4, 45, 99, 22, 99, 45, 10] 
b=set(lista)
c=list(b)
print(c)

#12
