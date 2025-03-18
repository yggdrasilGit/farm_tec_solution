# Classe Fertilizante que herda de Insumo
from manager.insumo_manage import Insumo


class Fertilizante(Insumo):
    def __init__(self, nome, descricao, quantidade, unidade, preco_unitario, tipo, composicao, dosagem_recomendada):
        super().__init__(nome, descricao, quantidade, unidade)
        self.preco_unitario = preco_unitario
        self.tipo = tipo
        self.composicao = composicao
        self.dosagem_recomendada = dosagem_recomendada

    def verificar_dosagem(self):
        return f"Dosagem recomendada: {self.dosagem_recomendada}"

    def calcular_valor_total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return "\n".join([
            f"Fertilizante: {self.tipo}",
            f"Composição: {self.composicao}",
            super().__str__(),
            f"Dosagem recomendada: {self.dosagem_recomendada}",
            f"Preço unitário: R${self.preco_unitario:.2f}"
        ])