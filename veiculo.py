class Veiculo:
    def __init__(self, placa, valor):
        self.placa = placa
        self.valor = valor
        self.alugado = False
        self.historico = []

    def alugar(self, cliente, dias):
        if self.alugado:
            return f"O veículo {self.placa} já está alugado."

        self.alugado = True
        aluguel = self.calcular_aluguel(dias)
        self.historico.append(
            f"Alugado para {cliente.nome} por {dias} dia(s) ao valor de R$ {aluguel:.2f}"
        )
        return f"Veículo {self.placa} alugado para {cliente.nome} por R$ {aluguel:.2f}"

    def devolver(self):
        if not self.alugado:
            return f"O veículo {self.placa} não está alugado."

        self.alugado = False
        self.historico.append("Devolvido.")
        return f"Veículo {self.placa} devolvido com sucesso."

    def listar_historico(self):
        if not self.historico:
            return f"Não há histórico para o veículo {self.placa}."
        return f"Histórico do veículo {self.placa}:\n" + "\n".join(self.historico)

    def calcular_aluguel(self, dias):
        raise NotImplementedError("O método calcular_aluguel deve ser implementado na classe derivada.")
