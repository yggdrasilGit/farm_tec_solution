# Classe Insumo
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
            f"Quantidade: {self.quantidade} {self.unidade}"
        ])


# Classe para gerenciar os insumos
class InsumoManager:
    def __init__(self):
        self.insumos = []  # Lista para armazenar insumos

    def create(self, nome, descricao, quantidade, unidade):
        # Criar um novo insumo e adicionar à lista
        novo_insumo = Insumo(nome, descricao, quantidade, unidade)
        self.insumos.append(novo_insumo)
        print(f"Insumo '{nome}' criado com sucesso!")

    def read(self, nome):
        # Buscar insumo pelo nome
        for insumo in self.insumos:
            if insumo["nome"] == nome:
                return insumo
        return None

    def update(self, nome, descricao=None, quantidade=None, unidade=None):
        # Atualizar um insumo existente
        insumo = self.read(nome)
        if insumo:
            if descricao:
                insumo["descricao"] = descricao
            if quantidade:
                insumo[quantidade] = quantidade
            if unidade:
                insumo[unidade] = unidade
            print(f"Insumo '{nome}' atualizado com sucesso!")
        else:
            print(f"Insumo '{nome}' não encontrado.")

    def delete(self, nome):
        # Deletar um insumo
        insumo = self.read(nome)
        if insumo:
            self.insumos.remove(insumo)
            print(f"Insumo '{nome}' deletado com sucesso!")
        else:
            print(f"Insumo '{nome}' não encontrado.")

    def list_all(self):
        # Listar todos os insumos
        if not self.insumos:
            print("Nenhum insumo registrado.")
        else:
            for insumo in self.insumos:
                print(insumo)