# Classe Fertilizante que herda de Insumo
from manager.insumos_manager import Insumo


class Fertilizante(Insumo):
    def __init__(self, nome, descricao, quantidade, unidade,
                preco_unitario, tipo, composicao, dosagem_recomendada):
        # Chama o construtor da classe base Insumo
        super().__init__(nome, descricao, quantidade, unidade)
        self.preco_unitario = preco_unitario  # Preço unitário do fertilizante
        self.tipo = tipo  # Tipo do fertilizante (ex.: "Nitrogenado", "Fosfatado")
        self.composicao = composicao  # Composição química do fertilizante (ex.: "NPK 10-20-10")
        self.dosagem_recomendada = dosagem_recomendada  # Dosagem recomendada por área

    def verificar_dosagem(self):
        # Método para verificar a dosagem recomendada para uso
        return f"Dosagem recomendada: {self.dosagem_recomendada}"

    def calcular_valor_total(self):
        # Método para calcular o valor total
        return self.quantidade * self.preco_unitario

    def __str__(self):
        # Método para representar o fertilizante de maneira legível
        return "\n".join([
            f"Fertilizante: {self.tipo}",
            f"Composição: {self.composicao}",
            super().__str__(),
            f"Dosagem recomendada: {self.dosagem_recomendada}",
            f"Preço unitário: R${self.preco_unitario:.2f}"
        ])
