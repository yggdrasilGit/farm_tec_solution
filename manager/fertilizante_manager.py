from manager.insumo_manage import Insumo


class Fertilizante(Insumo):
    """
    Classe que representa um fertilizante, herdando os atributos básicos de um insumo
    e adicionando características específicas como preço, tipo, composição e dosagem recomendada.
    """
    def __init__(self, nome, descricao, quantidade, unidade, preco_unitario, tipo, composicao, dosagem_recomendada):
        """
        Inicializa um novo objeto Fertilizante.

        Args:
            nome (str): Nome do fertilizante.
            descricao (str): Descrição do fertilizante.
            quantidade (int): Quantidade disponível do fertilizante.
            unidade (str): Unidade de medida do fertilizante (ex: "kg", "L").
            preco_unitario (float): Preço por unidade do fertilizante.
            tipo (str): Tipo do fertilizante (ex: "Orgânico", "Químico").
            composicao (str): Composição química do fertilizante.
            dosagem_recomendada (str): Dosagem recomendada para o uso do fertilizante.
        """
        super().__init__(nome, descricao, quantidade, unidade)
        self.preco_unitario = preco_unitario
        self.tipo = tipo
        self.composicao = composicao
        self.dosagem_recomendada = dosagem_recomendada

    def __str__(self):
        """
        Retorna uma string representando as informações detalhadas do fertilizante.

        Returns:
            str: String com as informações do fertilizante formatadas.
        """
        return "\n".join([
            f"Fertilizante: {self.tipo}",
            f"Composição: {self.composicao}",
            super().__str__(),
            f"Dosagem recomendada: {self.dosagem_recomendada}",
            f"Preço unitário: R${self.preco_unitario:.2f}"
        ])

    def to_dict(self):
        """
        Converte o objeto Fertilizante em um dicionário, incluindo todos os atributos 
        específicos desta classe.

        Returns:
            dict: Dicionário representando o objeto Fertilizante.
        """
        dados_insumo = super().to_dict()  # Chama o to_dict da classe pai (Insumo)
        dados_insumo.update({
            "preco_unitario": self.preco_unitario,
            "tipo": self.tipo,
            "composicao": self.composicao,
            "dosagem_recomendada": self.dosagem_recomendada,
            "tipo_insumo": "fertilizante"  # Identificador do tipo de insumo
        })
        return dados_insumo
