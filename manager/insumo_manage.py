class Insumo:
    def __init__(self, nome, descricao, quantidade, unidade):
        self.nome = nome  # Nome do insumo
        self.descricao = descricao  # Descrição do insumo
        self.quantidade = quantidade  # Quantidade disponível
        self.unidade = unidade  # Unidade de medida do insumo

    def __str__(self):
        # Método para representar o insumo de maneira legível
        return "\n".join([
            f"Insumo: {self.nome}",
            f"Descrição: {self.descricao}",
            f"Quantidade: {self.quantidade}", 
            f"Unidade: {self.unidade}"
        ])