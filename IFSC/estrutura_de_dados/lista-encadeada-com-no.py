from no import no

class listaEncadeada:
 def __init__ (self):
  self.primeiro = None # cabeca da lista

 def insere_inicio(self, valor):
  novo = no(valor) #cria um novo no
  novo.proximo = self.primeiro #o campo proximo do novo elemento deve apontar para o primeiro elemento da lista
  self.primeiro = novo #a cabeca da lista aponta para o novo

 def show(self):
    if self.primeiro == None:
     print ("esta vazio")
     return None



 def umespaco(self):
  print("\n")

v = listaEncadeada()
v.insere_inicio(0)
v.insere_inicio(2)
v.insere_inicio(3)
v.show()     