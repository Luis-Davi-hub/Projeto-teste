#class Aluno:
   # def __init__(self, nome, idade):
      #  self.nome = nome
     #   self.idade = idade

  #  def apresentar(self):
  #      print("Olá, meu nome é", self.nome)
     #   print("Tenho", self.idade, "anos.")


#aluno1 = Aluno("João", 16)

#aluno1.apresentar()

# Classe base
class Entrega:
    def __init__(self, cliente, endereco):
        self.cliente = cliente
        self.__endereco = endereco  

    def calcular_frete(self):
        return 0

    def mostrar_entrega(self):
        print("Cliente:", self.cliente)
        print("Endereço:", self.__endereco)
        print("Frete: R$", self.calcular_frete())



class EntregaNormal(Entrega):
    def calcular_frete(self):
        return 10.00


class EntregaExpressa(Entrega):
    def calcular_frete(self):
        return 20.00


entrega1 = EntregaNormal("João", "Rua A, 100")
entrega2 = EntregaExpressa("Maria", "Rua B, 200")

# Polimorfismo
entrega1.mostrar_entrega()
print()
entrega2.mostrar_entrega()
