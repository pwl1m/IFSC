class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
# Crie as seguintes funcoes (m´etodos):
# Calcula media, retornando a media aritmetica entre as notas;
# Mostra dados, que somente imprime o valor de todos os atributos;
# Resultado, que verifica se o aluno esta aprovado ou reprovado (se a
# media for maior ou igual a 6.0, o aluno esta aprovado)

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