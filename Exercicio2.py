from abc import ABC, abstractmethod

# Interface Torcedor
class Torcedor(ABC):
    @abstractmethod
    def torcer(self):
        pass

# Implementação da interface
class Corinthians(Torcedor):
    def torcer(self):
        print("Vai Corinthians!")

class Palmeiras(Torcedor):
    def torcer(self):
        print("Vai Palmeiras!")

# Teste do polimorfismo
torcedores = [Corinthians(), Palmeiras()]
for torcedor in torcedores:
    torcedor.torcer()
