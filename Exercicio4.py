# Classes de pizza sem polimorfismo
class PizzaCalabresa:
    def preparar(self):
        print("Ingredientes: molho, queijo, calabresa, cebola e tomate")

    def assar(self):
        print("Assando por 15 minutos...")

    def cobrar(self):
        print("R$ 12,00")

class PizzaNapolitana:
    def preparar(self):
        print("Ingredientes: molho, queijo, tomate e manjericão")

    def assar(self):
        print("Assando por 10 minutos...")

    def cobrar(self):
        print("R$ 15,00")

# Classe Forno sem polimorfismo
class Forno:
    def fabricar_calabresa(self, pizza):
        pizza.preparar()
        pizza.assar()
        pizza.cobrar()

    def fabricar_napolitana(self, pizza):
        pizza.preparar()
        pizza.assar()
        pizza.cobrar()

# Teste
forno = Forno()
forno.fabricar_calabresa(PizzaCalabresa())
forno.fabricar_napolitana(PizzaNapolitana())
