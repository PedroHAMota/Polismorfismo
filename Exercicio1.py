# Classe base Torcedor
class Torcedor:
    def torcer(self):
        print("Torcendo genericamente...")

# Classes filhas herdando de Torcedor
class Corinthians(Torcedor):
    def torcer(self):
        print("Vai Corinthians!")

class Santos(Torcedor):
    def torcer(self):
        print("Vai Santos!")

class Palmeiras(Torcedor):
    def torcer(self):
        print("Vai Palmeiras!")

# Teste do polimorfismo
torcedores = [Corinthians(), Santos(), Palmeiras()]
for torcedor in torcedores:
    torcedor.torcer()
