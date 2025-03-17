# Classe Insumo
class Insumo:
    def __init__(self, nome, descricao, quantidade, unidade):
        self.nome = nome  # Nome do insumo
        self.descricao = descricao  # Descrição do insumo
        self.quantidade = quantidade  # Quantidade disponível
        self.unidade = unidade  # Unidade de medida do insumo

    def __str__(self):
        # Método para representar o insumo de maneira legível
        return f"Insumo: {self.nome}, Descrição: {self.descricao}, Quantidade: {self.quantidade}, Unidade: {self.unidade}"

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
            if insumo.nome == nome:
                return insumo
        return None

    def update(self, nome, descricao=None, quantidade=None, unidade=None):
        # Atualizar um insumo existente
        insumo = self.read(nome)
        if insumo:
            if descricao:
                insumo.descricao = descricao
            if quantidade:
                insumo.quantidade = quantidade
            if unidade:
                insumo.unidade = unidade
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

# Exemplo de uso
manager = InsumoManager()

# Criando insumos
manager.create("Fertilizante A", "Fertilizante para plantas", 50, "kg")
manager.create("Semente B", "Semente de milho", 200, "unidade")

# Listando todos os insumos
print("\nTodos os Insumos:")
manager.list_all()

# Lendo um insumo específico
print("\nLendo Insumo 'Semente B':")
insumo = manager.read("Semente B")
if insumo:
    print(insumo)

# Atualizando um insumo
manager.update("Fertilizante A", quantidade=60)

# Deletando um insumo
manager.delete("Semente B")

# Listando todos os insumos após o delete
print("\nTodos os Insumos após o delete:")
manager.list_all()
