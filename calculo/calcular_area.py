import math
from manager.culture_manager import Cultura

class CalculadoraAreaCultura:
    def __init__(self):
        """
        Recebe uma instância da classe Cultura.
        """
        self.cultura = Cultura()

    def selecionar_cultura(self):
        """
        Exibe as culturas cadastradas e permite que o usuário selecione uma.
        Retorna o nome da cultura selecionada ou None se não houver seleção válida.
        """
        if not self.cultura._coluna_de_culturas:
            print("Nenhuma cultura cadastrada para seleção.")
            return None
        
        print("\nCulturas disponíveis:")
        for i, cult in enumerate(self.cultura._coluna_de_culturas, start=1):
            print(f"{i}. {cult.title()}")
        
        while True:
            escolha = input("Selecione a cultura pelo número: ")
            try:
                idx = int(escolha) - 1
                if idx < 0 or idx >= len(self.cultura._coluna_de_culturas):
                    print("Opção inválida! Tente novamente.")
                else:
                    return self.cultura._coluna_de_culturas[idx]
            except ValueError:
                print("Entrada inválida! Digite um número válido.")

    def calcular_area(self):
        """
        Permite que o usuário escolha o tipo de forma geométrica e insira os
        parâmetros necessários para calcular a área.
        Retorna a área calculada (em metros quadrados) ou None se houver erro.
        """
        print("\nEscolha o tipo de forma para calcular a área:")
        print("1. Retângulo")
        print("2. Círculo")
        print("3. Quadrado")
        
        while True:
            opcao = input("Opção: ")
            if opcao == '1':
                try:
                    largura = float(input("Digite a largura (m): "))
                    comprimento = float(input("Digite o comprimento (m): "))
                    area = largura * comprimento
                    return area
                except ValueError:
                    print("Entrada inválida para retângulo. Tente novamente.")
            elif opcao == '2':
                try:
                    raio = float(input("Digite o raio (m): "))
                    area = math.pi * (raio ** 2)
                    return area
                except ValueError:
                    print("Entrada inválida para círculo. Tente novamente.")
            elif opcao == '3':
                try:
                    lado = float(input("Digite o lado (m): "))
                    area = lado ** 2
                    return area
                except ValueError:
                    print("Entrada inválida para quadrado. Tente novamente.")
            else:
                print("Opção inválida! Tente novamente.")

    def executar(self):
        """
        Executa o processo de seleção de cultura e cálculo da área,
        exibindo os resultados.
        """
        cultura_selecionada = self.selecionar_cultura()
        if cultura_selecionada is None:
            return None  # Retorna None caso não haja seleção de cultura
        
        print(f"\nCultura selecionada para calcular: {cultura_selecionada}")
        area = self.calcular_area()
        if area is not None:
            print(f"\nÁrea calculada para '{cultura_selecionada}': {area:.2f} m²")
            # Retorna o tipo de roça (cultura) e a área calculada
            return (cultura_selecionada, area)  
        else:
            print("Falha no cálculo da área.")
            return None  # Retorna None caso o cálculo da área falhe
