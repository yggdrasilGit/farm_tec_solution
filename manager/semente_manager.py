# Classe Semente que herda de Insumo
from manager.insumo_manage import Insumo


class Semente(Insumo):
    def __init__(self, nome, descricao, quantidade, unidade, tipo, origem, validade):
        super().__init__(nome, descricao, quantidade, unidade)
        self.tipo = tipo
        self.origem = origem
        self.validade = validade

    def verificar_validade(self):
        return f"Semente {self.tipo} válida até: {self.validade}"

    def __str__(self):
        return f"Semente: {self.tipo}, Origem: {self.origem}, Validade: {self.validade}\n{super().__str__()}"

