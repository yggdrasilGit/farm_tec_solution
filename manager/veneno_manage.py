from manager.insumos_manager import InsumoManager

class Veneno(InsumoManager):
    def __init__(self, 
                 nome, 
                 descricao, 
                 quantidade, 
                 preco_unitario, 
                 tipo, 
                 toxicidade, 
                 area_aplicacao):
        
        # Chama o construtor da classe base Insumo
        super().__init__(nome, 
                         descricao, 
                         quantidade, 
                         preco_unitario)
        
        self.tipo = tipo  # Tipo de veneno (ex.: "Pesticida", "Herbicida")
        self.toxicidade = toxicidade  # Toxicidade do veneno (ex.: "Alta", "Média", "Baixa")
        self.area_aplicacao = area_aplicacao  # Área recomendada para aplicação (ex.: "Fazenda", "Jardim")

    def verificar_toxicidade(self):
        # Método para verificar a toxicidade do veneno
        return f"Nível de toxicidade: {self.toxicidade}"

    def __str__(self):
        # Método para representar o veneno de maneira legível
        return f"Veneno: {self.tipo}, Toxicidade: {self.toxicidade}, Área de Aplicação: {self.area_aplicacao}, {super().__str__()}"

# Criando um veneno que é um insumo
veneno1 = Veneno("Herbicida X", "Herbicida para controle de plantas daninhas", 100, 50.0, "Herbicida", "Alta", "Fazenda")

# Imprimindo o veneno (incluindo as informações do insumo)
print(veneno1)

# Calculando o valor total
print(f"Valor Total: R${veneno1.calcular_valor_total()}")
