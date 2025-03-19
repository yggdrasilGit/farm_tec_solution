class Insumo:
    def __init__(self, nome, descricao, quantidade, unidade):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.unidade = unidade

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidade": self.quantidade,
            "unidade": self.unidade
        }

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nUnidade: {self.unidade}"
