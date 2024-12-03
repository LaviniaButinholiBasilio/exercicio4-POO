from veiculo import Veiculo

class Moto(Veiculo):
    def calcular_aluguel(self, dias):
        aluguel = self.valor * dias
        if dias > 30:
            aluguel *= 1.2
        elif dias >= 10:
            aluguel *= 1.1
        return aluguel
