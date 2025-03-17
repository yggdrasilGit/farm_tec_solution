class Insumo:
    def __init__(self, nome, descricao, quantidade, preco_unitario):
        self.nome = nome  # Nome do insumo
        self.descricao = descricao  # Descrição do insumo
        self.quantidade = quantidade  # Quantidade disponível
        self.preco_unitario = preco_unitario  # Preço unitário do insumo

    def calcular_valor_total(self):
        # Método para calcular o valor total do insumo baseado na quantidade
        return self.quantidade * self.preco_unitario

    def __str__(self):
        # Método para representar o insumo de maneira legível
        return f"Insumo: {self.nome}, Descrição: {self.descricao}, Quantidade: {self.quantidade}, Preço Unitário: {self.preco_unitario}"
