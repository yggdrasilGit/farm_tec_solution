from manager.insumo_manage import Insumo


class Fertilizante(Insumo):
    def __init__(self, nome, descricao, quantidade, unidade, preco_unitario, tipo, composicao, dosagem_recomendada):
        super().__init__(nome, descricao, quantidade, unidade)
        self.preco_unitario = preco_unitario
        self.tipo = tipo
        self.composicao = composicao
        self.dosagem_recomendada = dosagem_recomendada

    def __str__(self):
        return "\n".join([
            f"Fertilizante: {self.tipo}",
            f"Composição: {self.composicao}",
            super().__str__(),
            f"Dosagem recomendada: {self.dosagem_recomendada}",
            f"Preço unitário: R${self.preco_unitario:.2f}"
        ])

    def to_dict(self):
        # Convertendo a classe para um dicionário, incluindo os atributos específicos de Fertilizante
        dados_insumo = super().to_dict()  # Chama o to_dict da classe pai (Insumo)
        dados_insumo.update({
            "preco_unitario": self.preco_unitario,
            "tipo": self.tipo,
            "composicao": self.composicao,
            "dosagem_recomendada": self.dosagem_recomendada,
            "tipo_insumo": "fertilizante"  # Identificador do tipo de insumo
        })
        return dados_insumo
