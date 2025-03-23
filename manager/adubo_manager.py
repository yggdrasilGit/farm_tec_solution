from manager.insumo_manage import Insumo

class Adubo(Insumo):
    """
    Representa um tipo de adubo derivado de Insumo.

    Atributos:
        tipo (str): Tipo de adubo (ex.: "Orgânico", "Mineral").
        forma_aplicacao (str): Forma de aplicação (ex.: "Granulado", "Líquido").
        dosagem_recomendada (str): Dosagem recomendada por área.
    """
    def __init__(self, nome, descricao, quantidade, unidade, tipo, forma_aplicacao, dosagem_recomendada):
        """
        Inicializa um objeto Adubo.
        
        Parâmetros:
            nome (str): Nome do adubo.
            descricao (str): Descrição do adubo.
            quantidade (float): Quantidade disponível.
            unidade (str): Unidade de medida.
            tipo (str): Tipo do adubo.
            forma_aplicacao (str): Forma de aplicação.
            dosagem_recomendada (str): Dosagem recomendada.
        """
        super().__init__(nome, descricao, quantidade, unidade)
        self.tipo = self.validar_tipo(tipo)
        self.forma_aplicacao = forma_aplicacao.strip().title()
        self.dosagem_recomendada = dosagem_recomendada
    
    @staticmethod
    def validar_tipo(tipo):
        """Valida o tipo do adubo, garantindo que seja Orgânico ou Mineral."""
        tipos_validos = {"Orgânico", "Mineral"}
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo inválido: {tipo}. Deve ser 'Orgânico' ou 'Mineral'.")
        return tipo

    def verificar_dosagem(self):
        """Retorna a dosagem recomendada para uso."""
        return f"Dosagem recomendada: {self.dosagem_recomendada}"

    def __str__(self):
        """Retorna uma representação legível do objeto Adubo."""
        return (f"Adubo: {self.tipo}, Forma de Aplicação: {self.forma_aplicacao}, "
                f"{super().__str__()}, Dosagem recomendada: {self.dosagem_recomendada}")

# Exemplo de uso:
# adubo1 = Adubo("Composto Orgânico", "Adubo orgânico para enriquecer o solo", 50, "kg", "Orgânico", "Granulado", "300g/m²")
# print(adubo1)
# print(adubo1.verificar_dosagem())