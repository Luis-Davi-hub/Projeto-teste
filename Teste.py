class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, meu nome é", self.nome)
        print("Tenho", self.idade, "anos.")


aluno1 = Aluno("João", 16)

aluno1.apresentar()
