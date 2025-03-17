# Classe base Insumo
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

# Classe derivada Fertilizante herda de Insumo
class Fertilizante(Insumo):
    def __init__(self, nome, descricao, quantidade, preco_unitario, tipo, composicao, dosagem_recomendada):
        # Chama o construtor da classe base Insumo
        super().__init__(nome, descricao, quantidade, preco_unitario)
        self.tipo = tipo  # Tipo do fertilizante (ex.: "Nitrogenado", "Fosfatado")
        self.composicao = composicao  # Composição química do fertilizante (ex.: "NPK 10-20-10")
        self.dosagem_recomendada = dosagem_recomendada  # Dosagem recomendada por área

    def verificar_dosagem(self):
        # Método para verificar a dosagem recomendada para uso
        return f"Dosagem recomendada: {self.dosagem_recomendada}"

    def __str__(self):
        # Método para representar o fertilizante de maneira legível
        return f"Fertilizante: {self.tipo}, Composição: {self.composicao}, {super().__str__()}, Dosagem recomendada: {self.dosagem_recomendada}"

# Criando um fertilizante que é um insumo
fertilizante1 = Fertilizante("Fosfato de Amônio", "Fertilizante utilizado para promover o crescimento das plantas", 30, 45.0, "Fosfatado", "NPK 20-20-0", "200g/m²")

# Imprimindo o fertilizante (incluindo as informações do insumo)
print(fertilizante1)

# Calculando o valor total
print(f"Valor Total: R${fertilizante1.calcular_valor_total()}")
