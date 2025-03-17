# Classe derivada Semente herda de Insumo
from manager.adubo_manager import Insumo


class Semente(Insumo):
    def __init__(self, nome, descricao, quantidade, unidade, tipo, origem, validade):
        # Chama o construtor da classe base Insumo
        super().__init__(nome, descricao, quantidade, unidade)
        self.tipo = tipo  # Tipo da semente (ex.: "milho", "feijão")
        self.origem = origem  # Origem da semente (ex.: "Brasil", "Argentina")
        self.validade = validade  # Data de validade da semente

    def verificar_validade(self):
        # Método para verificar se a semente ainda está dentro do prazo de validade
        return f"Semente {self.tipo} válida até: {self.validade}"

    def __str__(self):
        # Método para representar a semente de maneira legível
        return f"Semente: {self.tipo}, Origem: {self.origem}, Validade: {self.validade}, {super().__str__()}"

# Criando uma semente que é um insumo
semente1 = Semente("Arroz", "Insumo utilizado para alimentação", 50, 3.5, "Arroz", "Brasil", "2025-12-31")

# Imprimindo a semente (incluindo as informações do insumo)
print(semente1)

# Calculando o valor total
print(f"Valor Total: R${semente1.calcular_valor_total()}")
