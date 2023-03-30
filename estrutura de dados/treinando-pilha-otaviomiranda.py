# type annotation
from typing import List

# pilha de livros com type annotation
pilha_de_livros: List[str] = []  # 1

#adicionado livros no topo da pilha
pilha_de_livros.append ('livro 1') # 2
pilha_de_livros.append ('livro 2')
pilha_de_livros.append ('livro 3')


#usando o for
for livro in pilha_de_livros[::-1]: #inverte a ordem da pilha
    print(livro)


#obtendo o elemento mais novo
livro=pilha_de_livros.pop() # 3

#imprimindo
print('livro que retirei: ', livro)
print('livros restantes: ', pilha_de_livros)

# outro exemplo
pilha_de_pratos: List[int] = []

pilha_de_pratos.append (5)
pilha_de_pratos.append (4)
pilha_de_pratos.append (1)

recolheprato=pilha_de_pratos.pop()

print('prato recolido: ', recolheprato)
print('prato na mesa: ', pilha_de_pratos)