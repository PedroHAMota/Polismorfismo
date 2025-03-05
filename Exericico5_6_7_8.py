from abc import ABC, abstractmethod

# Interface Pizza
class Pizza(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def assar(self):
        pass

    @abstractmethod
    def cobrar(self):
        pass

# Implementação das pizzas
class Calabresa(Pizza):
    def preparar(self):
        print("Ingredientes: molho, queijo, calabresa, cebola e tomate")

    def assar(self):
        print("Assando por 15 minutos...")

    def cobrar(self):
        print("R$ 12,00")

class Napolitana(Pizza):
    def preparar(self):
        print("Ingredientes: molho, queijo, tomate e manjericão")

    def assar(self):
        print("Assando por 10 minutos...")

    def cobrar(self):
        print("R$ 15,00")

# Classe Forno polimórfica
class Forno:
    def fabricar(self, pizza: Pizza):
        pizza.preparar()
        pizza.assar()
        pizza.cobrar()

# Exercicio 6

class AlhoBacon(Pizza):
    def preparar(self):
        print("Ingredientes: molho, queijo, alho e bacon")

    def assar(self):
        print("Assando por 12 minutos...")

    def cobrar(self):
        print("R$ 18,00")

# Forno atualizado para permitir borda de catupiry
class Forno:
    def fabricar(self, pizza: Pizza, borda_catupiry=False):
        pizza.preparar()
        if borda_catupiry:
            print("Adicionando borda de catupiry...")
        pizza.assar()
        pizza.cobrar()

# Teste
forno = Forno()
forno.fabricar(Calabresa(), True)
forno.fabricar(Napolitana(), False)
forno.fabricar(AlhoBacon(), True)

# Exericicio 7
# Interface TipoPagamento
class TipoPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

# Implementações dos pagamentos
class Dinheiro(TipoPagamento):
    def pagar(self, valor):
        print("Pagamento em dinheiro. Não tem taxa!")

class CartaoCredito(TipoPagamento):
    def pagar(self, valor):
        print(f"Pagamento em cartão. Taxa de: R$ {valor * 0.20}")

class Boleto(TipoPagamento):
    def pagar(self, valor):
        print("Pagamento em boleto. Taxa fixa R$0,80")

# Classe Venda polimórfica
class Venda:
    def vender(self, pagamento: TipoPagamento, valor):
        pagamento.pagar(valor)

# Teste
venda = Venda()
venda.vender(Boleto(), 100)
venda.vender(CartaoCredito(), 100)
venda.vender(Dinheiro(), 100)

# Exercicio 8
# Interface Entrega
class Entrega(ABC):
    @abstractmethod
    def entregar(self, endereco):
        pass

# Implementação dos tipos de entrega
class Motoboy(Entrega):
    def entregar(self, endereco):
        print(f"Entrega via motoboy para {endereco}")

class Correios(Entrega):
    def entregar(self, endereco):
        print(f"Entrega via Correios para {endereco}")

class Transportadora(Entrega):
    def entregar(self, endereco):
        print(f"Entrega via Transportadora para {endereco}")

# Classe Pedido polimórfica
class Pedido:
    def realizar_entrega(self, entrega: Entrega, endereco):
        entrega.entregar(endereco)

# Teste
pedido = Pedido()
pedido.realizar_entrega(Motoboy(), "Rua A, 123")
pedido.realizar_entrega(Correios(), "Av. B, 456")
pedido.realizar_entrega(Transportadora(), "Travessa C, 789")

