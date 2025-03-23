class Insumo:
    """
    Classe base que representa um insumo, com informações básicas como nome, 
    descrição, quantidade e unidade de medida.
    """
    def __init__(self, nome, descricao, quantidade, unidade):
        """
        Inicializa um novo objeto Insumo.

        Args:
            nome (str): Nome do insumo.
            descricao (str): Descrição do insumo.
            quantidade (int): Quantidade disponível do insumo.
            unidade (str): Unidade de medida do insumo (ex: "kg", "L").
        """
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.unidade = unidade

    def to_dict(self):
        """
        Converte o objeto Insumo em um dicionário.

        Returns:
            dict: Dicionário com os atributos do insumo.
        """
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidade": self.quantidade,
            "unidade": self.unidade
        }

    def __str__(self):
        """
        Retorna uma string representando as informações do insumo.

        Returns:
            str: String formatada com os detalhes do insumo.
        """
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nUnidade: {self.unidade}"
