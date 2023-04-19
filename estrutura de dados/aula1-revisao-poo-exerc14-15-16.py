class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
    
    def resultado(self):
        media = self.calcular_media()
        if media >= 6.0:
            print("Aluno aprovado!")
        else:
            print("Aluno reprovado.")

# criando dois objetos Aluno
aluno1 = Aluno("João", 7.5, 8.0)
aluno2 = Aluno("Maria", 5.0, 6.0)

# testando as funções para aluno1
aluno1.mostrar_dados()
print("Média:", aluno1.calcular_media())
aluno1.resultado()

# testando as funções para aluno2
aluno2.mostrar_dados()
print("Média:", aluno2.calcular_media())
aluno2.resultado()
