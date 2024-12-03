from veiculo import Veiculo

class Carro(Veiculo):
    def calcular_aluguel(self, dias):
        return self.valor * dias
