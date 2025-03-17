

# Classe derivada Adubo herda de Insumo
from manager.insumos_manager import InsumoManager


class Adubo(InsumoManager):
    def __init__(self, nome, descricao, quantidade, preco_unitario, tipo, forma_aplicacao, dosagem_recomendada):
        # Chama o construtor da classe base Insumo
        super().__init__(nome, descricao, quantidade, preco_unitario)
        self.tipo = tipo  # Tipo de adubo (ex.: "Orgânico", "Mineral")
        self.forma_aplicacao = forma_aplicacao  # Forma de aplicação (ex.: "Granulado", "Líquido")
        self.dosagem_recomendada = dosagem_recomendada  # Dosagem recomendada por área

    def verificar_dosagem(self):
        # Método para verificar a dosagem recomendada para uso
        return f"Dosagem recomendada: {self.dosagem_recomendada}"

    def __str__(self):
        # Método para representar o adubo de maneira legível
        return f"Adubo: {self.tipo}, Forma de Aplicação: {self.forma_aplicacao}, {super().__str__()}, Dosagem recomendada: {self.dosagem_recomendada}"

# Criando um adubo que é um insumo
adubo1 = Adubo("Composto Orgânico", "Adubo orgânico para enriquecer o solo", 50, 30.0, "Orgânico", "Granulado", "300g/m²")

# Imprimindo o adubo (incluindo as informações do insumo)
print(adubo1)

# Calculando o valor total
print(f"Valor Total: R${adubo1.calcular_valor_total()}")
